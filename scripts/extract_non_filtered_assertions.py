import os
import sys
import pandas as pd

specfuzzer_assertions_file = sys.argv[1]
invalid_post_conditions_csv = sys.argv[2]

# Read SpecFuzzer assertions file
with open(specfuzzer_assertions_file, 'r') as file:
    set1 = {line.strip() for line in file}

set1 = {item for item in set1 if item and not item.startswith('buckets=') and not item.startswith(
    'specs=') and not item.startswith('======') and not item.startswith(':::')}

# Read CSV file with post-conditions that Daikon considered invalid
df = pd.read_csv(invalid_post_conditions_csv)
set2 = set(df['invariant'].str.strip())

# Find difference
difference = set1 - set2

assertions_file_name = os.path.basename(specfuzzer_assertions_file)
print(f"Specs from {assertions_file_name}: {len(set1)}")
print(f"Filtered specs: {len(set1) - len(difference)}")

# Write remaining specifications to output file
if len(sys.argv) > 3:
    class_name = sys.argv[3]
    method_name = sys.argv[4]

    AUTOMATIC_IF_OUTPUT_DIR = 'output'
    output_directory = f'{AUTOMATIC_IF_OUTPUT_DIR}/{class_name}_{method_name}/specs'
    os.makedirs(output_directory, exist_ok=True)

    output_file = f'{output_directory}/{class_name}-{method_name}-specfuzzer-refined.assertions'

    with open(output_file, 'w') as file:
        file.write(f"buckets={len(difference)}\n")
        file.write(f"specs={len(difference)}\n")
        file.write('=====================================\n')
        for item in difference:
            file.write(f'{item}\n')
