import os
import sys
import pandas as pd

AUTOMATIC_IF_OUTPUT_DIR = 'output'

assertions_file = sys.argv[1]
filtered_specs_file = sys.argv[2]
class_name = sys.argv[3]
method_name = sys.argv[4]

output_directory = f'{AUTOMATIC_IF_OUTPUT_DIR}/{class_name}_{method_name}/specs'

with open(assertions_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

records = []
current_ppt = None
for line in lines:
    line = line.rstrip()
    if line.startswith('======'):
        current_ppt = None
        continue
    if ':::' in line:
        current_ppt = line
    else:
        records.append({'invariant': line, 'ppt': current_ppt})

assertions_df = pd.DataFrame(records)
assertions_df['invariant'] = assertions_df['invariant'].astype(str)

specs_df = pd.read_csv(filtered_specs_file)
filtered_specs_list = specs_df['invariant'].dropna().unique().tolist()

is_in_filtered_specs = assertions_df['invariant'].isin(filtered_specs_list)
non_filtered_df = assertions_df[~is_in_filtered_specs]
filtered_df = assertions_df[is_in_filtered_specs]

print(f"Specs from {os.path.basename(assertions_file)}: {len(assertions_df)}")
print(f"Filtered specs: {len(filtered_df['invariant'].unique())}")

ppt_sequence = []
for ppt in assertions_df['ppt']:
    if ppt is not None and ppt not in ppt_sequence:
        ppt_sequence.append(ppt)

output_file = f'{output_directory}/{class_name}-{method_name}-specfuzzer-refined.assertions'

with open(output_file, 'w', encoding='utf-8') as file:
    for ppt in ppt_sequence:
        group = non_filtered_df[non_filtered_df['ppt'] == ppt]
        if group.empty:
            continue
        file.write(
            '===========================================================================\n')
        file.write(f'{ppt}\n')
        for inv in group['invariant']:
            file.write(f'{inv}\n')
