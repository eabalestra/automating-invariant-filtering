import glob
import os
import sys
import re
from typing import List
from code_extractor import extract_package_path
from test_extractor import extract_tests_from_file


def rename_test_methods(test_methods: List[str], new_name: str) -> List[str]:
    name_pattern = r'public void \w+\(\)'
    return [
        re.sub(name_pattern, f'public void {new_name}{i}()', test_method)
        for i, test_method in enumerate(test_methods)
    ]


def add_throws_declaration(test_methods: List[str]) -> List[str]:
    pattern = r'(public void \w+\(\))\s*(?:throws\s+[^\\{]*)?\s*\{'
    replacement = r'\1 throws Throwable {'

    updated_tests = []
    for test in test_methods:
        test = re.sub(pattern, replacement, test)
        updated_tests.append(test)
    return updated_tests


def replace_class_references(test_list: List[str], subject_class: str) -> List[str]:
    subject_package = extract_package_path(subject_class)
    subject_dir = os.path.dirname(subject_class)
    package_files = glob.glob(os.path.join(subject_dir, '*.java'))

    updated_tests = []
    for test in test_list:
        for file in package_files:
            file_name = os.path.basename(file).replace('.java', '')
            if f"{subject_package}.{file_name}" not in test:
                test = test.replace(
                    file_name, f"{subject_package}.{file_name}", -1)
        updated_tests.append(test)

    return updated_tests


def add_test_signatures(test_methods: List[str]) -> List[str]:
    updated_tests = []
    for test in test_methods:
        if not "@Test" in test:
            test = f"@Test\n{test}"
        updated_tests.append(test)
    return updated_tests


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python fix_llm_tests.py <output_dir> <source_test_suite> <subject_class>.java <method_name>")
        sys.exit(1)

    output_dir = sys.argv[1]
    source_test_suite = sys.argv[2]
    subject_class = sys.argv[3]
    method_name = sys.argv[4]

    class_name = os.path.basename(subject_class).replace('.java', '')
    fixed_test_suite = os.path.join(
        output_dir, f"{class_name}_{method_name}LlmFixedTest.java")

    test_suite = extract_tests_from_file(source_test_suite)
    if not test_suite:
        print(f"No tests found in {source_test_suite}")
        sys.exit(1)

    renamed_tests = rename_test_methods(test_suite, 'llmTest')
    updated_tests = replace_class_references(renamed_tests, subject_class)
    repaired_tests = add_throws_declaration(updated_tests)
    fixed_tests = add_test_signatures(repaired_tests)

    print(f"Processing {len(test_suite)} tests from {source_test_suite}")
    print(f"Repaired tests: {len(fixed_tests)}")
    print(f"Writing repaired tests to {fixed_test_suite}")

    for test in fixed_tests:
        with open(fixed_test_suite, "a") as file:
            file.write(test + "\n")
