import sys
import pandas as pd
from re import search
#from spec_processor import *

specs_file = sys.argv[1]
specs_and_mutants_file = sys.argv[2]

print(specs_file)
print(specs_and_mutants_file)


def is_inv_line(line):
    return not (search(":::OBJECT", line) or search("==============", line) or search(":::EXIT", line) or search(":::ENTER", line))

specs = []
with open(specs_file, "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        if is_inv_line(line):
            specs.append(line)
    specs = set(specs)
    #specs.sort()

def is_of_interest(spec):
    curr_spec = spec
    if (curr_spec.startswith("FuzzedInvariant:")):
        curr_spec = curr_spec.replace("FuzzedInvariant:","")
    if ("daikon.Quant.memberOf" in spec):
        return True
    for inv in specs:
        if (curr_spec in inv):
            return True
    return False

specs_and_mutants_df = pd.read_csv(specs_and_mutants_file)
mutant_killing_specs = specs_and_mutants_df["invariant"].unique()
mutant_killing_specs = list(filter(is_of_interest, mutant_killing_specs))
#mutant_killing_specs.sort()

print(f"Total specs: {len(specs)}")
print(f"Total mutant-killing specs: {len(mutant_killing_specs)}")

non_mutant_killing_specs = list(set(specs) - set(mutant_killing_specs))

print(f"Total non-mutant-killing specs: {len(non_mutant_killing_specs)}")

w = set(mutant_killing_specs) - specs
if w != set():
    print(f"specs in mutant-killing specs that do not belong to the set of total specs: {w}")
    print("TODO: Where this specs come from?")

subject_name = specs_file.split("/")[-1].split(".")[0]

output_dir = "output/non-mutant-killing-assertions/"
output_file = output_dir + subject_name + ".assertions"
print(f"Writing specs in: {output_file}")

with open(output_file, "w") as file:
    for spec in non_mutant_killing_specs:
        #spec = replace_spec_variables(spec)
        #spec = strip_outer_parentheses(spec)
        file.write(spec + "\n")
