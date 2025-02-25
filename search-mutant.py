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

# Load test suite
# TODO: load from a test file all the test one by one (should be sys.argv[3])
# example = """    @Test
#     public void llmTest2() throws Throwable {
#         DataStructures.StackAr stackAr0 = new DataStructures.StackAr(200);
#         stackAr0.push((java.lang.Object) 0L);
#         stackAr0.push((java.lang.Object) 0L);
#         stackAr0.push((java.lang.Object) 0L);
#         stackAr0.pop();
#     }"""
test_suite = test_extractor.extract_tests_from_file(sys.argv[3])

# Read the specs file
# likely_valid_specs = spec_reader.read_and_filter_specs(specs_file)
# TODO: use the script to read all the non mutant killing specs
# non_mutant_killing_specs = [sys.argv[4]]
non_mutant_killing_specs = spec_reader.read_and_filter_specs(sys.argv[4])

# create the output file
# output_test_dir = os.path.join(output_dir, "test")
# os.makedirs(output_test_dir, exist_ok=True)
# generated_test_suite = os.path.join(output_test_dir, f"{class_name}_{method_name}LlmTest.java")

mutation_attempts = 1
for spec in non_mutant_killing_specs:
    print(f"Generating mutant for spec: {spec}")
    spec = spec_processor.update_specification_variables(spec, class_name)
    for test in test_suite:
        for i in range(mutation_attempts):
            mutation = mutant_generator.generate_mutant(code, test, spec)
            print(mutation)
            # save response to a file in the output directory
            # f.write(final_test + "\n")
