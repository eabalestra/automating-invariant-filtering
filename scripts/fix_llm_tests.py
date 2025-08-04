import glob
import os
import sys
import re

from typing import List

from scripts.code_extractor import get_java_package_name
from scripts.test_extractor import extract_tests_from_file


def rename_test_methods(test_methods: List[str], new_name: str) -> List[str]:
    name_pattern = r"public void \w+\(\)"
    return [
        re.sub(name_pattern, f"public void {new_name}{i}()", test_method)
        for i, test_method in enumerate(test_methods)
    ]


def add_throws_declaration(test_methods: List[str]) -> List[str]:
    pattern = r"(public void \w+\(\))\s*(?:throws\s+[^\\{]*)?\s*\{"
    replacement = r"\1 throws Throwable {"

    updated_tests = []
    for test in test_methods:
        test = re.sub(pattern, replacement, test)
        updated_tests.append(test)
    return updated_tests


def replace_class_references(test_list: List[str], subject_class: str) -> List[str]:
    subject_package = get_java_package_name(subject_class)
    subject_dir = os.path.dirname(subject_class)
    package_files = glob.glob(os.path.join(subject_dir, "*.java"))

    updated_tests = []
    for test in test_list:
        for file in package_files:
            file_name = os.path.basename(file).replace(".java", "")
            if f"{subject_package}.{file_name}" not in test:
                test = test.replace(file_name, f"{subject_package}.{file_name}", -1)
        updated_tests.append(test)

    return updated_tests


def add_test_signatures(test_methods: List[str]) -> List[str]:
    updated_tests = []
    for test in test_methods:
        if not "@Test" in test:
            test = f"@Test\n{test}"
        updated_tests.append(test)
    return updated_tests


def rename_test_method(test_method: str, new_name: str, index: int) -> str:
    if new_name.strip() == "":
        return test_method
    name_pattern = r"public void \w+\(\)"
    return re.sub(name_pattern, f"public void {new_name}{index}()", test_method)


def add_throws_declaration_to_test(test_method: str) -> str:
    pattern = r"(public void \w+\(\))\s*(?:throws\s+[^\\{]*)?\s*\{"
    replacement = r"\1 throws Throwable {"
    return re.sub(pattern, replacement, test_method)


def replace_class_references_in_test(test_method: str, subject_class: str) -> str:
    subject_package = get_java_package_name(subject_class)
    subject_dir = os.path.dirname(subject_class)
    package_files = glob.glob(os.path.join(subject_dir, "*.java"))

    updated = test_method
    for file in package_files:
        file_name = os.path.basename(file).replace(".java", "")
        qualified = f"{subject_package}.{file_name}"
        # Only replace if not already qualified
        updated = re.sub(rf"\b{file_name}\b", qualified, updated)
    return updated


def add_test_signature_to_test(test_method: str) -> str:
    if test_method.strip() == "":
        return test_method
    if not test_method.strip().startswith("@Test"):
        return f"@Test\n{test_method}"
    return test_method


def repair_unit_test(
    raw_test: str, class_name: str, method_name: str, test_index: int
) -> str:
    t1 = rename_test_method(raw_test, method_name, test_index)
    t2 = replace_class_references_in_test(t1, class_name)
    t3 = add_throws_declaration_to_test(t2)
    t4 = add_test_signature_to_test(t3)
    return t4


# Example usage:
# for i, raw_test in enumerate(extract_tests_from_file(source_test_suite)):
#     t1 = rename_test_method(raw_test, 'llmTest', i)
#     t2 = replace_class_references_in_test(t1, subject_class)
#     t3 = add_throws_declaration_to_test(t2)
#     t4 = add_test_signature_to_test(t3)
#     final = repair_unit_test(t4, class_name, method_name)
#     # write final to file or collect


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python fix_llm_tests.py <output_dir> <source_test_suite> <subject_class>.java <method_name>"
        )
        sys.exit(1)

    output_dir = sys.argv[1]
    source_test_suite = sys.argv[2]
    subject_class = sys.argv[3]
    method_name = sys.argv[4]

    class_name = os.path.basename(subject_class).replace(".java", "")
    fixed_test_suite_path = os.path.join(
        output_dir, f"{class_name}_{method_name}LlmFixedTest.java"
    )

    raw_test_suite = extract_tests_from_file(source_test_suite)
    if not raw_test_suite:
        print(f"No tests found in {source_test_suite}")
        sys.exit(1)

    fixed_test_suite = []
    for i, raw_test in enumerate(raw_test_suite):
        fixed_test = repair_unit_test(raw_test, class_name, method_name, i)
        fixed_test_suite.append(fixed_test)

    # renamed_tests = rename_test_methods(raw_test_suite, 'llmTest')
    # updated_tests = replace_class_references(renamed_tests, subject_class)
    # repaired_tests = add_throws_declaration(updated_tests)
    # fixed_tests = add_test_signatures(repaired_tests)

    print(f"Processing {len(raw_test_suite)} tests from {source_test_suite}")
    print(f"Repaired tests: {len(fixed_test_suite)}")
    print(f"Writing repaired tests to {fixed_test_suite_path}")

    for fixed_test in fixed_test_suite:
        with open(fixed_test_suite_path, "a") as file:
            file.write(fixed_test + "\n")
