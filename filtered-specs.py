import sys
import os
from subprocess import call
from scripts import spec_processor

call("./scripts/init_env.sh", shell=True)

subject = sys.argv[1]
specs_dir = os.getenv('SPECS_DIR')
cls = sys.argv[2]
method = sys.argv[3] 

orig_specs_file = f'{specs_dir}/{subject}/output/{cls}-{method}-specfuzzer-1-buckets.assertions' 
refined_specs_file = f'output/{cls}_{method}/specs/{cls}-{method}-specfuzzer-refined.assertions'

orig_specs = []
with open(orig_specs_file) as f:
    for line in f.readlines():
        if '=====' in line or ':::' in line or 'buckets=' in line or 'specs=' in line:
            continue
        orig_specs.append(line.strip())
    
refined_specs = []
with open(refined_specs_file) as f:
    for line in f.readlines():
        if '=====' in line or ':::' in line:
            continue
        refined_specs.append(line.strip())

filtered_specs = set(orig_specs) - set(refined_specs)

print(f'orig_specs={len(orig_specs)}')
print(f'filtered_specs={len(filtered_specs)}')
for s in filtered_specs:
    print(spec_processor.update_specification_variables(s, cls))
