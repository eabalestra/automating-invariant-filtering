import sys
import pandas as pd

specs_file = sys.argv[1]
specs_and_mutants_file = sys.argv[2]

print(specs_file)
print(specs_and_mutants_file)

specs = []
with open(specs_file, "r") as file:
    specs = file.read().splitlines()
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
print(f"specs in mutant-killing specs that do not belong to the set of total specs: {w}")
print("TODO: Where this specs come from?")
