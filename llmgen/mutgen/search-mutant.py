import sys
import os
from mutgen import mutant_generator
from scripts import attr_and_method_extractor, spec_processor, spec_reader, test_extractor

# Load file and arguments
class_file = sys.argv[1]
method_name = sys.argv[2]
code = attr_and_method_extractor.extract_class_attributes_and_method(
    class_file, method_name)

class_name = os.path.basename(class_file).replace('.java', '')

# Read the specs file
non_mutant_killing_specs = spec_reader.read_and_filter_specs(sys.argv[3])

# create the output file
output_dir = sys.argv[4]
output_mutant_dir = os.path.join(output_dir, "llm")
os.makedirs(output_mutant_dir, exist_ok=True)
mutation_file = os.path.join(
    output_mutant_dir, f"{class_name}_{method_name}LlmGeneratedMutants.txt")

mutation_attempts = 1
with open(mutation_file, 'a') as f:
    for spec in non_mutant_killing_specs:
        print(f"Original spec: {spec}")
        spec = spec_processor.update_specification_variables(spec, class_name)
        print(f"calling llm for spec: {spec}")
        for i in range(mutation_attempts):
            mutation = mutant_generator.generate_mutant(code, spec)
            print(mutation)
            # save response to a file in the output directory
            f.write(mutation + '\n')

