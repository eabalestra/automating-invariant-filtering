from llmgen.Prompt import PromptID
from llmgen.testgen.LLMTestGenerator import LLMTestGenerator
from llmgen.utils.string_utils import list_of_strings

from scripts import spec_processor, spec_reader, test_extractor
from scripts import code_extractor

import argparse
import logging
import os
import time

from scripts.fix_llm_tests import repair_unit_test
from scripts.test_compiler import TestCompiler


def add_spec_comment(code: str, spec: str) -> str:
    test_method_start = code.find("@Test")
    if test_method_start == -1:
        return code

    method_body_start = code.find("{", test_method_start)
    if method_body_start == -1:
        return code

    specification_comment = "\n    // Spec: " + spec
    code_before_brace = code[: method_body_start + 1]
    code_after_brace = code[method_body_start + 1 :]
    modified_code = code_before_brace + specification_comment + code_after_brace

    return modified_code


def parse_args():
    parser = argparse.ArgumentParser(
        prog="TestGen",
        description="Generates unit tests that attempt to override specifications for a Java method using LLM.",
        epilog="",
    )

    parser.add_argument("output_dir", help="Output directory path")
    parser.add_argument("subject_class", help="Path to the Java class file")
    parser.add_argument("specs_file", help="Path to the specifications file")
    parser.add_argument("method_name", help="Name of the method to test")
    parser.add_argument(
        "original_test_suite_path", help="Path to the original test suite file"
    )

    parser.add_argument(
        "-m",
        "--models",
        type=list_of_strings,
        dest="models_list",
        default="",
        help="List the LLMs to run.",
        metavar="MODELS",
    )

    parser.add_argument(
        "-sw",
        "--starts-with",
        type=str,
        dest="models_prefix",
        default=None,
        help="Selects all LLMs starting with the <prefix>.",
        metavar="PREFIX",
    )

    parser.add_argument(
        "-p",
        "--prompts",
        type=list_of_strings,
        dest="prompts_list",
        default="",
        help="List the prompts to use.",
        metavar="PROMPTS",
    )

    parser.add_argument(
        "-ll",
        "--llms",
        "--llm-list",
        dest="list_llms",
        action="store_true",
        help="List the supported LLMs.",
    )

    parser.add_argument(
        "-pl",
        "--prompt-list",
        dest="list_prompts",
        action="store_true",
        help="List the available prompts.",
    )

    return parser.parse_args()


def configure_logging():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO
    )


def select_models(llm_service, models_list, models_prefix):
    # include only supported models
    models = []
    if models_prefix is not None:
        models = llm_service.get_model_ids_startswith(models_prefix)
        if len(models) == 0:
            raise ValueError("Invalid models prefix.")
    else:
        if (
            models_list is None
            or models_list == ""
            or models_list == []
            or models_list == [""]
        ):
            models = llm_service.get_all_models()
        else:
            all_models = llm_service.get_all_models()
            for m in all_models:
                if m in models_list:
                    models.append(m)
        if len(models) == 0:
            raise ValueError("No model selected.")
    return models


def select_prompts(prompts_list):
    # include only supported prompts
    prompt_IDs = []
    if (
        prompts_list is None
        or prompts_list == ""
        or prompts_list == []
        or prompts_list == [""]
    ):
        prompt_IDs = PromptID.all()
    else:
        for p in prompts_list:
            for p1 in PromptID.all():
                if p == p1.name or "PromptID." + p == p1.name:
                    prompt_IDs.append(p1)
    return prompt_IDs


def main():
    args = parse_args()
    configure_logging()

    LLMrunner = LLMTestGenerator()

    if args.list_llms:
        print("Supported LLMs:", *LLMrunner.llm_service.get_all_models(), sep="\n")
        return
    if args.list_prompts:
        print("Available PromptIDs:", *[p.name for p in PromptID], sep="\n")
        return

    try:
        models = select_models(
            LLMrunner.llm_service, args.models_list, args.models_prefix
        )
        prompt_IDs = select_prompts(args.prompts_list)
    except ValueError as e:
        logging.error(e)
        return

    subject_class = args.subject_class
    class_code = open(subject_class, "r").read()
    method_code = code_extractor.extract_method_code(class_code, args.method_name)
    class_name = os.path.basename(subject_class).replace(".java", "")

    specs = spec_reader.read_and_filter_specs(args.specs_file)

    output_dir = args.output_dir
    output_test_dir = os.path.join(output_dir, "test")
    os.makedirs(output_test_dir, exist_ok=True)
    suite_file_path = os.path.join(
        output_test_dir, f"{class_name}_{args.method_name}LlmTest.java"
    )
    log_file_path = os.path.join(output_test_dir, "timestamps.log")

    logging.info(f"Model(s) used: {models}")
    logging.info(f"Prompt(s) used: {prompt_IDs}")

    compiler = TestCompiler(
        class_path=subject_class,
        suite_path=args.original_test_suite_path,
        method_name=args.method_name,
    )

    total_time = 0.0
    with open(suite_file_path, "a") as suite, open(log_file_path, "w") as log:
        for spec in specs:
            logging.info(f"Generating test for spec: {spec}")
            updated_spec = spec_processor.update_specification_variables(
                spec, class_name
            )

            start = time.time()
            llm_response = LLMrunner.generate_test(
                class_code=class_code,
                method_code=method_code,
                spec=updated_spec,
                prompt_ids=prompt_IDs,
                models_ids=models,
            )
            elapsed = time.time() - start
            total_time += elapsed

            logging.info(f"Generated response for spec: {spec}\n {llm_response}")

            # If the LLM response is not compilable, try to fix it
            test_code = spec_processor.remove_assertions_from_test(llm_response)
            test_code = test_extractor.extract_test_with_comments_from_string(test_code)
            fixed_test_code = repair_unit_test(test_code, class_name, "", 0)

            logging.error(f"Fixed test code: \n {fixed_test_code}")

            is_compilable, compilation_error = compiler.is_test_compilable(
                test_code=fixed_test_code
            )
            if not is_compilable:
                logging.warning("Test is not compilable.")
                test_code = LLMrunner.generate_test(
                    class_code=class_code,
                    method_code=method_code,
                    spec=llm_response + "\n" + compilation_error,
                    prompt_ids=[PromptID.NOT_COMPILABLE],
                    models_ids=models,
                )

            log.write(f"Time taken for LLM response for {spec}: {elapsed:.4f} sec")

            test_code = spec_processor.remove_assertions_from_test(test_code)
            test_code = test_extractor.extract_test_with_comments_from_string(test_code)
            test_code = add_spec_comment(test_code, spec)
            test_code = add_spec_comment(test_code, updated_spec)

            suite.write(test_code + "\n")

        log.write(
            f"\nTotal LLM time for {class_name}_{args.method_name}: {total_time:.4f} seconds\n"
        )


if __name__ == "__main__":
    main()
