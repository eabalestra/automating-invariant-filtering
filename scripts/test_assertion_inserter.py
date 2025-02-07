import re

def insert_assertion_into_test_code(test_code, specification):
    # generate the assertion from the specification
    assertion_statement = generate_assertion_from_specification(specification)
    
    # define a pattern to match any assertion
    assertion_pattern = re.compile(r'(?i)assert\w*\s*\(.*?\);', re.DOTALL)
    
    # replace ALL existing assertions with the new assertion
    test_code, num_subs = re.subn(assertion_pattern, assertion_statement, test_code)

    if num_subs == 0:
        end_of_method = re.compile(r'(\s*}\s*)', re.DOTALL)
        assertion = f'    {assertion_statement}\\1'
        test_code = re.sub(end_of_method, assertion, test_code)
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
    return '\n\n    assertTrue(' + specification + ');'