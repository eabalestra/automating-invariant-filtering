import sys
import pandas as pd

assertions_file = sys.argv[1]
filtered_specs_file = sys.argv[2]
# output_dir = sys.argv[3]
# class_name = sys.argv[4]
# method_name = sys.argv[5]

with open(assertions_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

records = []
current_ppt = None
for line in lines:
    line = line.rstrip()
    if line.startswith("======"):
        current_ppt = None
        continue
    if ":::" in line:
        current_ppt = line
    else:
        records.append({"invariant": line, "ppt": current_ppt})

assertions_df = pd.DataFrame(records)
assertions_df["invariant"] = assertions_df["invariant"].astype(str)

specs_df = pd.read_csv(filtered_specs_file)
filtered_specs_list = specs_df["invariant"].dropna().unique().tolist()

is_in_filtered_specs = assertions_df["invariant"].isin(filtered_specs_list)
non_filtered_df = assertions_df[~is_in_filtered_specs]
filtered_df = assertions_df[is_in_filtered_specs]

print(f"Specs from assertions file: {len(assertions_df)}")
print(f"Filtered specs: {len(filtered_df["invariant"].unique())}")

ppt_sequence = []
for ppt in assertions_df["ppt"]:
    if ppt is not None and ppt not in ppt_sequence:
        ppt_sequence.append(ppt)

with open("non_filtered_specs.assertions", "w", encoding="utf-8") as file:
    for ppt in ppt_sequence:
        group = non_filtered_df[non_filtered_df["ppt"] == ppt]
        if group.empty:
            continue
        file.write(
            "===========================================================================\n")
        file.write(f"{ppt}\n")
        for inv in group["invariant"]:
            file.write(f"{inv}\n")


# data = {"invariant": ["A", "B", "C", "D"]}
# assertions_df = pd.DataFrame(data)
# print(assertions_df["invariant"])
# filtered_specs_list = ["A", "C", "E"]
# print("")

# is_not_filtered = ~assertions_df["invariant"].isin(set(filtered_specs_list))
# print(is_not_filtered)

# assertions_df = assertions_df[is_not_filtered]
# print("")
# print(assertions_df["invariant"])
