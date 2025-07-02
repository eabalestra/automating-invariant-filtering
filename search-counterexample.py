import argparse
import sys
import os
import time

from scripts import spec_processor, spec_reader, test_extractor, code_extractor
from testgen.LLMTestGenerator import LLMTestGenerator
from testgen.Prompt import PromptID


def list_of_strings(arg):
    return arg.split(',')


def add_spec_to_test(code, spec_str):
    test_method_start = code.find("@Test")
    if test_method_start == -1:
        return code

    method_body_start = code.find("{", test_method_start)
    if method_body_start == -1:
        return code

    specification_comment = "\n    // Spec: " + spec_str
    code_before_brace = code[:method_body_start + 1]
    code_after_brace = code[method_body_start + 1:]
    modified_code = code_before_brace + specification_comment + code_after_brace

    return modified_code


if __name__ == "__main__":
    import sys
    print(f"Debug: sys.argv = {sys.argv}")
    
    parser = argparse.ArgumentParser(
        prog='TestGen',
        description='Generates unit tests that attempt to override specifications for a Java method using LLM.',
        epilog='')

    parser.add_argument("output_dir", help="Output directory path")
    parser.add_argument("subject_class", help="Path to the Java class file")
    parser.add_argument("specs_file", help="Path to the specifications file")
    parser.add_argument("method_name", help="Name of the method to test")

    parser.add_argument("-m", "--models", type=list_of_strings, dest="models_list",
                        default="", help="List the LLMs to run.", metavar="MODELS")

    parser.add_argument("-sw", '--starts-with', type=str, dest="models_prefix",
                        default=None, help="Selects all LLMs starting with the <prefix>.", metavar="PREFIX")

    parser.add_argument("-p", "--prompts", type=list_of_strings, dest="prompts_list",
                        default="", help="List the prompts to use.", metavar="PROMPTS")

    parser.add_argument('-ll', '--llms', "--llm-list", dest="list_llms",
                        action='store_true', help="List the supported LLMs.")

    parser.add_argument('-pl', "--prompt-list", dest="list_prompts",
                        action='store_true', help="List the available prompts.")

    args = parser.parse_args()
    
    print(f"Debug: args.models_list = {args.models_list}")
    print(f"Debug: args.models_prefix = {args.models_prefix}")
    print(f"Debug: args.prompts_list = {args.prompts_list}")
    print(f"Debug: type(args.models_list) = {type(args.models_list)}")

    output_dir = args.output_dir

    output_dir = args.output_dir
    subject_class = args.subject_class
    specs_file = args.specs_file
    method_name = args.method_name

    LLMrunner = LLMTestGenerator()

    # include only supported models
    models = []
    print(f"Debug: Checking models_prefix: {args.models_prefix}")
    if args.models_prefix is not None:
        models = LLMrunner.llm_service.get_model_ids_startswith(
            args.models_prefix)
        print(f"Debug: Models found with prefix: {models}")
        if len(models) == 0:
            raise parser.error("Invalid models prefix.")
    else:
        print(f"Debug: No prefix, checking models_list: {args.models_list}")
        if args.models_list is None or args.models_list == "" or args.models_list == [] or args.models_list == [""]:
            print("Debug: Using all models")
            models = LLMrunner.llm_service.get_all_models()
        else:
            print("Debug: Filtering models from list")
            all_models = LLMrunner.llm_service.get_all_models()
            print(f"Debug: All available models: {all_models}")
            for m in all_models:
                if m in args.models_list:
                    print(f"Debug: Adding model {m}")
                    models.append(m)
        print(f"Debug: Final models list: {models}")
        if len(models) == 0:
            raise parser.error("No model selected.")

    # include only supported prompts
    prompt_IDs = []
    if args.prompts_list is None or args.prompts_list == "" or args.prompts_list == [] or args.prompts_list == [""]:
        prompt_IDs = PromptID.all()
    else:
        for p in args.prompts_list:
            for p1 in PromptID.all():
                if p == p1.name or "PromptID."+p == p1.name:
                    prompt_IDs.append(p1)

    # Load class code and method code
    class_code = open(subject_class, 'r').read()
    method_code = code_extractor.extract_method_code(class_code, method_name)
    class_name = os.path.basename(subject_class).replace('.java', '')

    # Read the specs file
    likely_valid_specs = spec_reader.read_and_filter_specs(specs_file)

    # create the output file
    output_test_dir = os.path.join(output_dir, "test")
    os.makedirs(output_test_dir, exist_ok=True)
    generated_test_suite = os.path.join(
        output_test_dir, f"{class_name}_{method_name}LlmTest.java")

    # timestamp log
    llm_test_timestamp = os.path.join(output_test_dir, "timestamps.log")
    log = open(llm_test_timestamp, "w")

    test_attempts = 1
    total_time = 0.0

    if len(prompt_IDs) == 0:
        raise parser.error("No prompt selected.")

    with open(generated_test_suite, 'a') as f:
        for spec in likely_valid_specs:
            for i in range(test_attempts):
                print(f"Generating test for spec: {spec}")
                processed_spec = spec_processor.update_specification_variables(
                    spec, class_name)

                start_time = time.time()

                print(f"Model(s) used: {models}")
                print(f"Prompt(s) used: {prompt_IDs}")

                # Generate the tests using the different LLMs and prompts
                generated_test = LLMrunner.generate_test(
                    class_code=class_code, method_code=method_code, spec=processed_spec, prompt_ids=prompt_IDs, models_ids=models)

                print(f"Generated test: {generated_test}")

                end_time = time.time()
                elapsed_time = end_time - start_time
                total_time += elapsed_time
                log.write(
                    f"Time taken for LLM response for {spec}: {elapsed_time:.4f} sec\n")

                assertion_free_test = spec_processor.remove_assertions_from_test(
                    generated_test)
                final_test = test_extractor.extract_test_with_comments_from_string(
                    assertion_free_test)

                # Add two differents formats of the spec to the test
                final_test = add_spec_to_test(final_test, spec)
                final_test = add_spec_to_test(final_test, processed_spec)

                # save response to a file in the output directory
                f.write(final_test + "\n")

    log.write(
        f"\nTotal LLM time for {class_name}_{method_name}: {total_time:.4f} seconds\n")
    log.close()
