import re
from typing import List

from file_manager import read_file, write_file


def rename_classes_in_file(file_path: str) -> None:
    content = read_file(file_path, 'r')
    pattern = r'(public\s+class\s+)(\w+)(\s*\{)'
    replacement = r'\1\2Augmented\3'
    new_content = re.sub(pattern, replacement, content)
    write_file(file_path, new_content, 'w')


def rename_test_methods(test_methods: List[str], new_name: str) -> List[str]:
    name_pattern = r'public void \w+\(\)'
    return [
        re.sub(name_pattern, f'public void {new_name}{i}()', test_method)
        for i, test_method in enumerate(test_methods)
    ]
