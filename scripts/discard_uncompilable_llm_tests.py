
import os
import sys

from test_compiler import get_compilable_tests
from test_extractor import extract_tests_from_file


output_dir = sys.argv[1]
destination_test_suite = sys.argv[2]
subject_class = sys.argv[3]
method_name = sys.argv[5]

class_name = os.path.basename(subject_class).replace('.java', '')
compilable_test_suite = os.path.join(output_dir, f"{class_name}_{method_name}LlmCompilableTest.java")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(
            "Usage: python discard_uncompilable_llm_tests.py <output_dir> <destination_test_suite> <subject_class>.java <source_test_suite> <method_name>")
        sys.exit(1)

    repaired_tests = extract_tests_from_file(sys.argv[4])

    compiled_tests = get_compilable_tests(
        destination_test_suite, subject_class, repaired_tests)

    print(f"Compiled {len(compiled_tests)} tests")
    print(f"Writing compiled tests to {compilable_test_suite}")

    with open(compilable_test_suite, "a") as file:
        for test in compiled_tests:
            file.write(test + "\n")
