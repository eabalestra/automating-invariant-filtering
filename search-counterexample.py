import sys
import os
from testgen import test_generator
from scripts import assertion_remover, spec_processor, spec_reader, test_extractor, utils

OUTPUT_DIR = 'output/test/'

# Load file and arguments
class_file_path = sys.argv[1]
specs_file_path = sys.argv[2]
method_name = sys.argv[3]

# Load class code and method code
class_code = open(class_file_path, 'r').read()
method_code = utils.extract_method_code(class_code, method_name)
class_name = utils.extract_class_name(class_code)

likely_valid_specs = spec_reader.read_and_filter_specs(specs_file_path)

# create output dir for class cls
os.makedirs(os.path.join(OUTPUT_DIR, class_name), exist_ok=True)

# create the output file
test_suite_path = os.path.join(
    OUTPUT_DIR, class_name, f"{class_name}_{method_name}LlmTest.java")
with open(test_suite_path, "w") as file:
    pass

test_attempts = 1
for spec in likely_valid_specs:
    for i in range(test_attempts):
        print(f"Generating test for spec: {spec}")
        processed_spec = spec_processor.update_specification_variables(spec)
        generated_test = test_generator.generate_test(
            class_name, class_code, method_code, processed_spec)
        assertion_free_test = assertion_remover.strip_assertions_from_test_code(
            generated_test)
        final_test = test_extractor.extract_test_with_comments_from_string(
            assertion_free_test)
        # save response to a file in the output directory
        with open(test_suite_path, 'a') as f:
            f.write(final_test + '\n\n')
