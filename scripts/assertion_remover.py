import re

def remove_existing_assertions(test_code):
    # define a pattern to match any assertion provided by llm
    assertion_pattern = re.compile(r'^\s*(?:[a-zA-Z0-9_.]+\.)?(?:assert\w*\b.*?;|fail\w*\b.*?;).*$', re.MULTILINE | re.IGNORECASE)

    # remove all existing assertions
    test_code = re.sub(assertion_pattern, '', test_code)

    return test_code