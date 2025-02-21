import sys
import os
from testgen import test_generator
from scripts import assertion_remover, spec_processor, spec_reader, test_extractor, code_extractor

# Load file and arguments
output_dir, class_file, specs_file, method_name = sys.argv[1:5]

# Load class code and method code
class_code = open(class_file, 'r').read()
method_code = code_extractor.extract_method_code(class_code, method_name)
class_name = code_extractor.extract_class_name(class_code)

# Read the specs file
likely_valid_specs = spec_reader.read_and_filter_specs(specs_file)

# create the output file
output_test_dir = os.path.join(output_dir, "test")
os.makedirs(output_test_dir, exist_ok=True)
generated_test_suite = os.path.join(output_test_dir, f"{class_name}_{method_name}LlmTest.java")
with open(generated_test_suite, "w") as file:
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
        with open(generated_test_suite, 'a') as f:
            f.write(final_test + '\n\n')
