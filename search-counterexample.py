import sys
import os
from testgen import test_generator
from scripts import assertion_remover, spec_processor, spec_reader, test_extractor, code_extractor

# Load file and arguments
output_dir, subject_class, specs_file, method_name = sys.argv[1:5]

# Load class code and method code
class_code = open(subject_class, 'r').read()
method_code = code_extractor.extract_method_code(class_code, method_name)
class_name = os.path.basename(subject_class).replace('.java', '')

# Read the specs file
likely_valid_specs = spec_reader.read_and_filter_specs(specs_file)

# create the output file
output_test_dir = os.path.join(output_dir, "test")
os.makedirs(output_test_dir, exist_ok=True)
generated_test_suite = os.path.join(output_test_dir, f"{class_name}_{method_name}LlmTest.java")

test_attempts = 1
with open(generated_test_suite, 'a') as f:
    for spec in likely_valid_specs:
        for i in range(test_attempts):
            print(f"Generating test for spec: {spec}")
            processed_spec = spec_processor.update_specification_variables(spec)
            generated_test = test_generator.generate_test(class_name, class_code, method_code, processed_spec)
            assertion_free_test = assertion_remover.strip_assertions_from_test_code(generated_test)
            final_test = test_extractor.extract_test_with_comments_from_string(assertion_free_test)
            # save response to a file in the output directory
            f.write(final_test + "\n")
