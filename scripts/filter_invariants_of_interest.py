import os
import sys
import pandas as pd

AUTOMATIC_IF_OUTPUT_DIR = 'output'

specs_file = sys.argv[1]
full_qualifier = sys.argv[2]
class_name = full_qualifier.split(".")[1]
method_name = sys.argv[3]

output_directory = f"{AUTOMATIC_IF_OUTPUT_DIR}/{class_name}_{method_name}/specs"


def is_of_interest(ppt):
    if "ENTER" in ppt:
        return False
    obj_spec = f"{full_qualifier}.{class_name}("
    return (method_name in ppt) or (obj_spec in ppt)


input_specifications = pd.read_csv(specs_file)

interest_ppts = list(filter(is_of_interest, input_specifications["ppt"].unique()))

interest_filtered_specs = input_specifications[input_specifications["ppt"].isin(interest_ppts)]

output_file = f"{output_directory}/interest-specs.csv"

interest_filtered_specs.to_csv(output_file, index=False)
