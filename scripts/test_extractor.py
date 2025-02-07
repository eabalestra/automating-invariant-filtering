def extract_test(response_test):
    lines = response_test.split('\n')
    test_case_started = False
    test_case_ended = False
    extracted_test = []
    comments = []
    brace_count = 0

    for line in lines:
        if line.strip().startswith('@Test'):
            test_case_started = True
        if test_case_started:
            extracted_test.append(line)
            if '{' in line:
                brace_count += 1
            if '}' in line:
                brace_count -= 1
            if brace_count == 0 and line.strip().endswith('}'):
                test_case_ended = True
                test_case_started = False
        else:
            comments.append(f"// {line}")
    return '\n'.join(comments + extracted_test)