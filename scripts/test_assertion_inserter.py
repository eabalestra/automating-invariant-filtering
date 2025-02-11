import re
from scripts.spec_processor import normalize_spec

def insert_assertion_into_test_code(test_code, specification):
    # generate the assertion from the specification
    assertion_statement = generate_assertion_from_specification(specification)
    
    # define a pattern to match any assertion provided by llm
    assertion_pattern = re.compile(r'^\s*(?:[a-zA-Z0-9_.]+\.)?(?:assert\w*\b.*?;|fail\w*\b.*?;).*$', re.MULTILINE | re.IGNORECASE)

    # remove all existing assertions
    test_code = re.sub(assertion_pattern, '', test_code)

    # find the end of the method and insert the new assertion before it    
    end_of_test = re.compile(r'(\s*}\s*)', re.DOTALL)
    assertion = f'{assertion_statement}\\1'
    test_code = re.sub(end_of_test, assertion, test_code)

    return test_code

def generate_assertion_from_specification(specification):
    normalized_spec = normalize_spec(specification)
    return f'\n\n    assertTrue({normalized_spec});'