import re

def extract_test(response_test):
    lines = response_test.split('\n')
    test_case_started = False
    extracted_test = []
    comments = []
    brace_count = 0

    test_start_pattern = re.compile(r'^\s*@Test')
    brace_pattern = re.compile(r'[{}]')

    for line in lines:
        if test_start_pattern.match(line):
            test_case_started = True
        if test_case_started:
            extracted_test.append(line)
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and line.strip().endswith('}'):
                test_case_started = False
        else:
            comments.append(f"// {line}")
    return '\n'.join(comments + extracted_test)