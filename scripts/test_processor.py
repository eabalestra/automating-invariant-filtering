import re
from typing import List
from file_manager import read_file, write_file


def add_augmented_to_constructor_subject(file_path: str, subject_name: str) -> None:
    content = read_file(file_path, 'r')
    escaped_subject = re.escape(subject_name)
    pattern_regex = rf'\b({escaped_subject})(\b\s+\w+\s*=\s*new\s+)({escaped_subject})(\s*\()'
    replacement = r'\1Augmented\2\3Augmented\4'
    new_content = re.sub(pattern_regex, replacement, content)
    write_file(file_path, new_content, 'w')


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
