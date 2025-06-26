import os
import sys
import pandas as pd
import re

AUTOMATIC_IF_OUTPUT_DIR = 'output'

# Buckets assertions file from specfuzzer
specfuzzer_assertions_file = sys.argv[1]
# CSV file with invalid post-conditions from Daikon
invalid_post_conditions_csv = sys.argv[2]
class_name = sys.argv[3]
method_name = sys.argv[4]

output_directory = f'{AUTOMATIC_IF_OUTPUT_DIR}/{class_name}_{method_name}/specs'

with open(specfuzzer_assertions_file, 'r', encoding='utf-8') as file:
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
specfuzzer_buckets_specs_df = pd.DataFrame(records)
specfuzzer_buckets_specs_df['invariant'] = specfuzzer_buckets_specs_df['invariant'].astype(
    str)

# Create a dataframe for the specs that were filtered through Daikon with the newly generated tests traces
invalid_postconditions = pd.read_csv(invalid_post_conditions_csv)
invalid_specs = invalid_postconditions['invariant'].dropna().tolist()

# Obtain the specs that were not filtered out
is_spec_filtered = specfuzzer_buckets_specs_df['invariant'].isin(invalid_specs)

non_filtered_specs_df = specfuzzer_buckets_specs_df[~is_spec_filtered]
filtered_specs_df = specfuzzer_buckets_specs_df[is_spec_filtered]

# Commented out print statements for debugging purposes
# print(f"Specs from specfuzzer:")
# for inv in specfuzzer_buckets_specs_df['invariant']:
#     print(f"  {inv}")
# print("")

# print(f"Filtered specs from {invalid_post_conditions_csv}:")
# for inv in filtered_specs_df['invariant']:
#     print(f"  {inv}")
# print("")

# print(f"Non-filtered specs from {specfuzzer_assertions_file}:")
# for inv in non_filtered_specs_df['invariant']:
#     print(f"  {inv}")
# print("")

# Dont change this print because it is used in the collect_results.py script
print(
    f"Specs from {os.path.basename(specfuzzer_assertions_file)}: {len(specfuzzer_buckets_specs_df)}")
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
for ppt in specfuzzer_buckets_specs_df['ppt']:
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
