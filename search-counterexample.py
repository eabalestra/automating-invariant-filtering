import csv
import sys
import os
import re
from testgen import test_generator
from scripts import assertion_remover, test_extractor, spec_processor

OUTPUT_DIR = 'output/test/'

def extract_method_code(class_code, method_name):
    pattern = rf'public\s+[^\s]+\s+{method_name}\s*\(.*?\)\s*{{(?:[^{{}}]*|{{(?:[^{{}}]*|{{[^{{}}]*}})*}})*}}'
    match = re.search(pattern, class_code, re.DOTALL)
    if match:
        return match.group(0)
    else:
        raise ValueError(f"Method {method_name} not found in the provided class code.")

def extract_class_name(class_code):
    pattern = r'public\s+class\s+(\w+)'
    match = re.search(pattern, class_code)
    if match:
        return match.group(1)
    else:
        raise ValueError("Class name not found in the provided class code.")

# Load file and arguments
class_file_path=sys.argv[1]
specs_csv_file=sys.argv[2] # Csv file containing specifications.
method_name=sys.argv[3]

# Load class code and method code
class_code = open(class_file_path, 'r').read()
method_code = extract_method_code(class_code, method_name)
class_name = extract_class_name(class_code)

# read specs from a csv file
likely_valid_specs = []
with open(specs_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        likely_valid_specs.append(row['spec'])

# create output dir for class cls
os.makedirs(os.path.join(OUTPUT_DIR, class_name), exist_ok=True)

# create the output file
test_suite_path = os.path.join(OUTPUT_DIR, class_name, f"{class_name}_{method_name}-llm-tests.java")
with open(test_suite_path, "w") as file:
    pass

test_attempts = 1
for spec in likely_valid_specs:
    for i in range(test_attempts):
        print(f"Generating test for spec: {spec}")
        processed_spec = spec_processor.replace_spec_variables(spec)
        generated_test = test_generator.generate_test(class_name, class_code, method_code, processed_spec)
        assertion_free_test = assertion_remover.remove_existing_assertions(generated_test)
        final_test = test_extractor.extract_test(assertion_free_test)
        # save response to a file in the output directory
        with open(test_suite_path, 'a') as f:
            f.write(final_test + '\n\n')