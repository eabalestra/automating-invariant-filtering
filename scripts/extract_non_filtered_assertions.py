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

merged = specfuzzer_buckets_specs_df.merge(
    invalid_postconditions,
    how='left',
    indicator=True
)

refined_specs_df = merged[merged['_merge'] == 'left_only'].drop('_merge', axis=1)
deleted_specs_df = merged[merged['_merge'] == 'both'].drop('_merge', axis=1)

# TODO: Todo esto esta chatgpeteado. Pero anda, borra este comentario despues.
# Output of specfuzzer. It should be .assertions file, not buckets.assertions. Because we want to see how many specs were discarded from the total. Maybe the variable should be called specfuzzer_assertions_df.
print(specfuzzer_buckets_specs_df)
# This are the "invalid" assertions, it should be assertions because include class invariants and method postconditions. There are the invalid postconditions from .gz file, that means we can have more assertions than .assertions file.
print(invalid_postconditions)
# This df contains the assertions of specfuzzer output that are not in invalid_postconditions df. This is our final output.
print(refined_specs_df)
# This df contains the removed assertions from the original specfuzzer output. It is for debug purpose only.
print(deleted_specs_df)

# TODO: Acomodar de aca para abajo teniendo en cuenta los nuevos dataframes.

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
