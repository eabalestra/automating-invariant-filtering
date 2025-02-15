import re


def strip_assertions_from_test_code(test_code: str) -> str:
    assertion_regex = re.compile(
        r'^\s*(?:[a-zA-Z0-9_.]+\.)?(?:assert\w*\b.*?;|fail\w*\b.*?;).*$',
        re.MULTILINE | re.IGNORECASE
    )
    return re.sub(assertion_regex, '', test_code)
