import os
import sys
import pandas as pd

AUTOMATIC_IF_OUTPUT_DIR = 'output/test/'

specs_file = sys.argv[1]
full_qualifier = sys.argv[2]
class_name = full_qualifier.split(".")[1]
method_name = sys.argv[3]


def is_of_interest(ppt):
    if "ENTER" in ppt:
        return False
    obj_spec = f"{full_qualifier}.{class_name}("
    return (method_name in ppt) or (obj_spec in ppt)


input_specifications = pd.read_csv(specs_file)

interest_ppts = list(
    filter(is_of_interest, input_specifications["ppt"].unique()))

filtered_specs = input_specifications[input_specifications["ppt"].isin(
    interest_ppts)]

print(f"Total specs: {len(input_specifications['invariant'])}")
print(f"Filtered specs: {len(filtered_specs)}")

output_file_dir = f"{AUTOMATIC_IF_OUTPUT_DIR}"
output_file = f"{output_file_dir}{class_name}/specs.csv"

# Create the directory if it doesn't exist
os.makedirs(output_file_dir, exist_ok=True)

filtered_specs.to_csv(output_file, index=False)
print(f"Filtered specs written in: {output_file}")
