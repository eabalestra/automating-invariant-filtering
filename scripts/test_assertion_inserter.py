import re

def insert_assertion_into_test_code(test_code, specification):
    # generate the assertion from the specification
    assertion_statement = generate_assertion_from_specification(specification)
    
    # define a pattern to match any assertion provided by llm
    assertion_pattern = re.compile(r'^\s*(?:[a-zA-Z0-9_.]+\.)?(?:assert\w*\b.*?;|fail\w*\b.*?;).*$', re.MULTILINE | re.IGNORECASE)

    # remove all existing assertions
    test_code = re.sub(assertion_pattern, '', test_code)

    # find the end of the method and insert the new assertion before it    
    end_of_method = re.compile(r'(\s*}\s*)', re.DOTALL)
    assertion = f'{assertion_statement}\\1'
    test_code = re.sub(end_of_method, assertion, test_code)

    return test_code

def generate_assertion_from_specification(specification):
    specification = process_specification(specification)
    return f'\n\n    assertTrue({specification});'

def process_specification(specification):
    spec = strip_outer_parentheses(specification.strip())
    
    parts = split_outside_parentheses(spec, r'\s*xor\s*', max_splits=1)
    if len(parts) > 1:
        first = process_specification(parts[0])
        second = process_specification(parts[1])
        return f'(!({first} && {second}) && ({first} || {second}))'
    parts = split_outside_parentheses(spec, r'\s*(implies|==>)\s*', max_splits=1)
    if len(parts) > 1:
        left_spec = process_specification(parts[0])
        right_spec = process_specification(parts[1])
        return f'!({left_spec}) || ({right_spec})'
    parts = split_outside_parentheses(spec, r'\s*(iff|<=>)\s*', max_splits=1)
    if len(parts) > 1:
        left_spec = process_specification(parts[0])
        right_spec = process_specification(parts[1])
        return f'({left_spec}) == ({right_spec})'
    return spec

def strip_outer_parentheses(expr):
    expr = expr.strip()
    if expr.startswith('(') and expr.endswith(')'):
        depth = 0
        for i, ch in enumerate(expr):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if depth == 0 and i < len(expr) - 1:
                return expr
        return expr[1:-1].strip()
    return expr

def split_outside_parentheses(spec, op_regex, max_splits=1):
    parts = []
    current = []
    depth = 0
    splits = 0
    i = 0
    while i < len(spec):
        char = spec[i]
        if char == '(':
            depth += 1
            current.append(char)
            i += 1
        elif char == ')':
            depth -= 1
            current.append(char)
            i += 1
        else:
            if depth == 0:
                m = re.match(op_regex, spec[i:], re.IGNORECASE)
                if m:
                    parts.append(''.join(current).strip())
                    current = []
                    i += m.end()
                    splits += 1
                    if splits == max_splits:
                        current.append(spec[i:])
                        break
                    continue
                else:
                    current.append(char)
                    i += 1
            else:
                current.append(char)
                i += 1
    parts.append(''.join(current).strip())
    return parts