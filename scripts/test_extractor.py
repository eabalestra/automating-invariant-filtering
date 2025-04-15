import re
from typing import List, Tuple


def extract_test_with_comments_from_string(text: str) -> str:
    lines = text.split('\n')
    comments, extracted_test = parse_comments_and_test(lines)
    return '\n'.join(comments + extracted_test)


def extract_tests_from_file(source_test_file: str) -> List[str]:
    try:
        with open(source_test_file, "r", encoding='utf-8') as sf:
            content = sf.read()
        return parse_test_from_string(content)
    except FileNotFoundError:
        print(f"File not found: {source_test_file}")
        return []
    except Exception as e:
        print(f"Error reading file {source_test_file}: {e}")
        return []


def parse_comments_and_test(lines: List[str]) -> Tuple[List[str], List[str]]:
    test_case_started = False
    extracted_test = []
    comments = []
    brace_count = 0
    test_start_pattern = re.compile(r'^\s*@Test')

    for line in lines:
        if test_start_pattern.match(line):
            test_case_started = True
        if test_case_started:
            extracted_test.append(line)
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and line.strip().endswith('}'):
                extracted_test.append("\n")
                test_case_started = False
        else:
            comments.append(f"// {line}")
    return comments, extracted_test


def parse_test_from_string(content: str) -> List[str]:
    brace_count = 0
    test_methods = []
    extracted_test = []
    test_case_started = False
    lines = content.split('\n')
    test_start_pattern = re.compile(r'^\s*@Test')

    for line in lines:
        if test_start_pattern.match(line):
            test_case_started = True
        if test_case_started:
            extracted_test.append(line)
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and line.strip().endswith('}'):
                test_case_started = False
                test_methods.append('\n'.join(extracted_test))
                extracted_test = []
    return test_methods
