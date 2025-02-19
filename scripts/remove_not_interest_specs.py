import sys
import pandas as pd

OUTPUT_DIR = 'output/test/'

specs_file = sys.argv[1]
full_qualifier = sys.argv[2]
class_name = full_qualifier.split(".")[1]
method_name = sys.argv[3]


def is_of_interest(ppt):
    if not "EXIT" in ppt:
        return False
    obj_spec = f"{full_qualifier}.{class_name}("
    return (method_name in ppt) or (obj_spec in ppt)


input_specifications = pd.read_csv(specs_file)
input_program_points = input_specifications["ppt"].unique()
interest_specs = list(filter(is_of_interest, input_program_points))

relevant_specifications = list(set(input_program_points) - set(interest_specs))

output_file = f"{OUTPUT_DIR}{class_name}/{class_name}_{method_name}-interesting.filtered-specs"

with open(output_file, "w") as file:
    for spec in interest_specs:
        complete_spec = input_specifications[input_specifications["ppt"] == spec]
        complete_spec = complete_spec["invariant"].values[0]
        file.write(complete_spec + "\n")

print(f"Total filtered specs: {len(input_specifications)}")
print(f"Total non-interesting specs: {len(relevant_specifications)}")
print(f"Total interesting specs: {len(interest_specs)}")
print(f"Writing specs in: {output_file}")
