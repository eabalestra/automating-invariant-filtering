import sys
import re
from typing import List

from utils import append_test_method_to_file, extract_package_path
from test_compiler import check_if_test_compiles
from test_extractor import extract_tests_from_file


def rename_test_methods(test_methods: List[str], new_name: str) -> List[str]:
    name_pattern = r'public void \w+\(\)'
    return [
        re.sub(name_pattern, f'public void {new_name}{i}()', test_method)
        for i, test_method in enumerate(test_methods)
    ]


def replace_method_calling(test_methods: List[str], subject_package: str) -> List[str]:
    constructor_pattern = r'new\s+(?!' + \
        re.escape(subject_package) + r'\.)([A-Z]\w*)\('
    static_call_pattern = r'(?<!' + \
        re.escape(subject_package) + r'\.)\b([A-Z]\w*)\.'
    type_declaration_pattern = r'(?<!@)(?<!' + \
        re.escape(subject_package) + r'\.)\b([A-Z]\w*)\b'

    new_tests = []
    for test in test_methods:
        unqualified_constructor = re.search(constructor_pattern, test)
        unqualified_static = re.search(static_call_pattern, test)
        unqualified_type = re.search(type_declaration_pattern, test)

        if not (unqualified_constructor or unqualified_static or unqualified_type):
            new_tests.append(test)
        else:
            test = re.sub(constructor_pattern,
                          f'new {subject_package}.\\1(', test)
            test = re.sub(static_call_pattern, f'{subject_package}.\\1.', test)
            test = re.sub(type_declaration_pattern,
                          f'{subject_package}.\\1', test)
            new_tests.append(test)
    return new_tests


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python script.py <destination_test_file> <source_test_file>")
        sys.exit(1)

    destination_test_file, source_test_file, subject_file = sys.argv[1:4]
    test_methods = extract_tests_from_file(source_test_file)
    subject_package = extract_package_path(subject_file)

    if not test_methods:
        return
    test_methods = rename_test_methods(test_methods, 'llmTest')
    test_methods = replace_method_calling(test_methods, subject_package)
    for test_method in test_methods:
        if check_if_test_compiles(destination_test_file, subject_file, test_method):
            append_test_method_to_file(destination_test_file, test_method)


if __name__ == "__main__":
    main()
