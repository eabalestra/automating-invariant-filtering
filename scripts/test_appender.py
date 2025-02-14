import sys
import re
from typing import List

from test_extractor import extract_tests_from_file

def append_test_method_to_file(destination_file: str, test_method: str) -> None:
    try:
        with open(destination_file, 'r+', encoding='utf-8') as df:
            content = df.read()
            if '}' not in content:
                print("No closing brace '}' found in the existing test file.")
                return
            head, tail = content.rsplit('}', 1)
            new_content = f"{head}\n{test_method}\n}}{tail}"
            df.seek(0)
            df.write(new_content)
            df.truncate()
    except IOError as e:
        print(f'Error processing file {destination_file}: {e}')

def rename_test_methods(test_methods: List[str], new_name:str) -> List[str]:
    name_pattern = r'public void \w+\(\)'
    return [
        re.sub(name_pattern, f'public void {new_name}{i}()', test_method)
        for i, test_method in enumerate(test_methods)
    ]

def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python script.py <destination_test_file> <source_test_file>")
        sys.exit(1)

    destination_test_file, source_test_file = sys.argv[1:3]
    test_methods = extract_tests_from_file(source_test_file)

    if not test_methods:
        return

    test_methods = rename_test_methods(test_methods, 'llmTest')
    for test_method in test_methods:
        append_test_method_to_file(destination_test_file, test_method)

if __name__ == "__main__":
    main()
