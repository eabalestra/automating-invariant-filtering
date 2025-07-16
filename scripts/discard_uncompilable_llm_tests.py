import os
import sys

from test_compiler import TestCompiler
from test_extractor import extract_tests_from_file

class_name = sys.argv[1]
method_name = sys.argv[2]
class_path = sys.argv[3]
destination_test_suite = sys.argv[4]
source_test_suite = sys.argv[5]
output_dir = sys.argv[6]

compilable_test_suite = os.path.join(
    output_dir, f"{class_name}_{method_name}LlmCompilableTest.java")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print(
            "Usage: python discard_uncompilable_llm_tests.py <output_dir> <destination_test_suite> <subject_class>.java <source_test_suite> <method_name>")
        sys.exit(1)

    print(f"Extracting tests from {source_test_suite}")

    repaired_tests = extract_tests_from_file(source_test_suite)

    compiler = TestCompiler(class_path, destination_test_suite, method_name)
    compiled_tests = compiler.get_compilable_tests(repaired_tests)

    print(f"Compiled {len(compiled_tests)} tests")
    print(f"Writing compiled tests to {compilable_test_suite}")

    with open(compilable_test_suite, "a") as file:
        for test in compiled_tests:
            file.write(test + "\n")
