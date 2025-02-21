import os
import sys
import re
from typing import List
from code_extractor import extract_package_path
from test_extractor import extract_tests_from_file

output_dir = sys.argv[1]
source_test_suite = sys.argv[2]
subject_class = sys.argv[3]
method_name = sys.argv[4]


def rename_test_methods(test_methods: List[str], new_name: str) -> List[str]:
    name_pattern = r'public void \w+\(\)'
    return [
        re.sub(name_pattern, f'public void {new_name}{i}()', test_method)
        for i, test_method in enumerate(test_methods)
    ]


def prepare_tests_for_compilation(tests, source_test_suite, subject_class) -> List[str]:
    print(f"Processing {len(tests)} tests from {source_test_suite}")

    subject_name = os.path.basename(subject_class).replace('.java', '')
    subject_package = extract_package_path(subject_class)

    renamed_tests = rename_test_methods(tests, 'llmTest')
    updated_tests = replace_method_calling(
        renamed_tests, subject_package, subject_name)

    return add_throws_declaration(updated_tests)


def replace_method_calling(test_methods: List[str], subject_package: str, subject: str) -> List[str]:
    escaped_subject = re.escape(subject)

    constructor_pattern = r'new\s' + escaped_subject + r'\('
    static_call_pattern = r'\b' + escaped_subject + r'\.'
    type_declaration_pattern = r'\b' + escaped_subject + r'\s+([a-zA-Z]\w*)\b'

    updated_tests = []
    for test in test_methods:
        if re.search(constructor_pattern, test) and not re.search(r'new\s' + re.escape(subject_package) + r'\.' + escaped_subject + r'\(', test):
            replacement = f'new {subject_package}.{subject}('
            test = re.sub(constructor_pattern, replacement, test)
        if re.search(static_call_pattern, test) and not re.search(r'\b' + re.escape(subject_package) + r'\.' + escaped_subject + r'\.', test):
            replacement = f'{subject_package}.{subject}.'
            test = re.sub(static_call_pattern, replacement, test)
        if re.search(type_declaration_pattern, test) and not re.search(r'\b' + re.escape(subject_package) + r'\.' + escaped_subject + r'\s+([a-zA-Z]\w*)\b', test):
            replacement = f'{subject_package}.{subject} \\1'
            test = re.sub(type_declaration_pattern, replacement, test)
        updated_tests.append(test)

    return updated_tests


def add_throws_declaration(test_methods: List[str]) -> List[str]:
    pattern = r'(public void \w+\(\))\s*(?:throws\s+[^\\{]*)?\s*\{'
    replacement = r'\1 throws Throwable {'

    updated_tests = []
    for test in test_methods:
        test = re.sub(pattern, replacement, test)
        updated_tests.append(test)
    return updated_tests


class_name = os.path.basename(subject_class).replace('.java', '')
fixed_test_suite = os.path.join(
    output_dir, f"{class_name}_{method_name}LlmFixedTest.java")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python fix_llm_tests.py <output_dir> <source_test_suite> <subject_class>.java <method_name>")
        sys.exit(1)

    source_test_suite = sys.argv[2]

    test_suite = extract_tests_from_file(source_test_suite)

    if not test_suite:
        print(f"No tests found in {source_test_suite}")
        sys.exit(1)

    repaired_tests = prepare_tests_for_compilation(
        test_suite, source_test_suite, subject_class)

    print(f"Repaired tests: {len(repaired_tests)}")
    print(f"Writing repaired tests to {fixed_test_suite}")

    for test in repaired_tests:
        with open(fixed_test_suite, "a") as file:
            file.write(test + "\n")
