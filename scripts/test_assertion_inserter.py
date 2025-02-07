import re

def insert_assertion_into_test_code(test_code, specification):
    # extract the assertion condition from the specification
    assertion_statement = generate_assertion_from_specification(specification)
    # define a pattern to match any assertion
    assertion_pattern = re.compile(r'assert\w*\((?:[^)(]+|\((?:[^)(]+|\([^)(]*\))*\))*\);')
    # replace all existing assertions with the new assertion
    test_code = re.sub(assertion_pattern, assertion_statement, test_code, count=1)

    if not re.search(assertion_pattern, test_code):
        test_code = re.sub(r'(\s*}\s*)$', f'\n    {assertion_statement}\n\\1', test_code)
    return test_code

def generate_assertion_from_specification(specification):
    if 'implies' in specification or '==>' in specification:
        parts = re.split(r'\s*implies\s*|\s*==>\s*', specification)
        specification = f'!({parts[0]}) || ({parts[1]})'
    elif 'iff' in specification or '<=>' in specification:
        parts = re.split(r'\s*iff\s*|\s*<=>\s*', specification)
        specification = f'({parts[0]}) == ({parts[1]})'
    elif 'xor' in specification:
        parts = re.split(r'\s*xor\s*', specification)
        specification = f'(!({parts[0]} && {parts[1]}) && ({parts[0]} || {parts[1]}))'
    return 'assertTrue(' + specification + ');'