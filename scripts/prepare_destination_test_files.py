import os
import sys
import re
from file_manager import read_file, write_file


def add_augmented_to_constructor_subject(file_path: str, subject_name: str) -> None:
    content = read_file(file_path, 'r')
    escaped_subject = re.escape(subject_name)
    pattern_regex = rf'\b({escaped_subject})(\b\s+\w+\s*=\s*new\s+)({escaped_subject})(\s*\()'
    replacement = r'\1Augmented\2\3Augmented\4'
    new_content = re.sub(pattern_regex, replacement, content)
    write_file(file_path, new_content, 'w')


def rename_classes_in_file(file_path: str) -> None:
    content = read_file(file_path, 'r')
    pattern = r'(public\s+class\s+)(\w+)(\s*\{)'
    replacement = r'\1\2Augmented\3'
    new_content = re.sub(pattern, replacement, content)
    write_file(file_path, new_content, 'w')


def prepare_destination_files(destination_test_driver: str, destination_test_suite: str) -> None:
    rename_classes_in_file(destination_test_suite)
    rename_classes_in_file(destination_test_driver)
    tester_class_name = os.path.basename(
        destination_test_suite).replace('Augmented.java', '')
    add_augmented_to_constructor_subject(
        destination_test_driver, tester_class_name)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python prepare_destination_test_files.py <destination_suite>.java <destination_driver>.java")
        sys.exit(1)

    destination_test_suite, destination_test_driver = sys.argv[1:3]

    prepare_destination_files(destination_test_driver, destination_test_suite)
