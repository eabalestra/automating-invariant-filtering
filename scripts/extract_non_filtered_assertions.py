import os
import sys
import pandas as pd
import re

AUTOMATIC_IF_OUTPUT_DIR = 'output'

buckets_assertions_file = sys.argv[1]
filtered_specs_file = sys.argv[2]
class_name = sys.argv[3]
method_name = sys.argv[4]

output_directory = f'{AUTOMATIC_IF_OUTPUT_DIR}/{class_name}_{method_name}/specs'

with open(buckets_assertions_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

records = []
current_ppt = None
for line in lines:
    line = line.rstrip()
    if line.startswith('buckets'):
        current_ppt = None
        continue
    if line.startswith("specs"):
        current_ppt = None
        continue
    if line.startswith('======'):
        current_ppt = None
        continue
    if ':::' in line:
        current_ppt = line
    else:
        records.append({'invariant': line, 'ppt': current_ppt})

# Create a DataFrame for the specs that existed before the test generation
specs_before_test_gen_df = pd.DataFrame(records)
specs_before_test_gen_df['invariant'] = specs_before_test_gen_df['invariant'].astype(
    str)

# Create a dataframe for the specs that were filtered through Daikon with the newly generated tests traces
specs_after_test_gen_df = pd.read_csv(filtered_specs_file)
filtered_specs = specs_after_test_gen_df['invariant'].dropna().tolist()

# Obtain the specs that were not filtered out
spec_is_filtered = specs_before_test_gen_df['invariant'].isin(filtered_specs)

non_filtered_specs_df = specs_before_test_gen_df[~spec_is_filtered]
filtered_specs_df = specs_before_test_gen_df[spec_is_filtered]

print(
    f"Specs from {os.path.basename(buckets_assertions_file)}: {len(specs_before_test_gen_df)}")
print(f"Filtered specs: {len(filtered_specs_df['invariant'])}")

original_buckets = 0
original_specs = 0

for line in lines:
    if line.startswith('buckets='):
        match = re.search(r'buckets=(\d+)', line)
        if match:
            original_buckets = int(match.group(1))
    if line.startswith('specs='):
        match = re.search(r'specs=(\d+)', line)
        if match:
            original_specs = int(match.group(1))

remaining_specs = len(non_filtered_specs_df)

ppt_sequence = []
for ppt in specs_before_test_gen_df['ppt']:
    if ppt is not None and ppt not in ppt_sequence:
        ppt_sequence.append(ppt)

output_file = f'{output_directory}/{class_name}-{method_name}-specfuzzer-refined.assertions'

with open(output_file, 'w', encoding='utf-8') as file:
    # Write header with updated counts
    file.write(f"buckets={remaining_specs}\n")
    file.write(f"specs={remaining_specs}\n")

    # Write the invariants for each program point
    for ppt in ppt_sequence:
        group = non_filtered_specs_df[non_filtered_specs_df['ppt'] == ppt]
        if group.empty:
            continue
        file.write('=====================================\n')
        file.write(f'{ppt}\n')
        for inv in group['invariant']:
            file.write(f'{inv}\n')
