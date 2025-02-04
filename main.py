import csv
import sys
import os
import re
from testgen import test_generator

output_dir = 'output/test/'

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
cls=sys.argv[1]
csv_file=sys.argv[2] # Csv file containing specifications.
method_name=sys.argv[3]

# Load class code and method code
class_code = open(cls, 'r').read()
method_code = extract_method_code(class_code, method_name)
class_name = extract_class_name(class_code)

# read specs from a csv file
likely_valid_specs = []
with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        likely_valid_specs.append(row['spec'])

test_suite_path = os.path.join(output_dir, class_name, 'TestSuite.java')
with open(test_suite_path, "w") as file:
    pass

tries = 3
for spec in likely_valid_specs:
    for i in range(tries):
        test = test_generator.generate_test(class_name, class_code, method_code, spec)
        # save response to a file in the output directory
        os.makedirs(os.path.join(output_dir, class_name), exist_ok=True)
        with open(test_suite_path, 'a') as f:
            f.write(test+'\n\n')
