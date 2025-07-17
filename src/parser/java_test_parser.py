import re
from typing import List, Tuple


class JavaTestParser:
    def __init__(self):
        self.test_start_pattern = re.compile(r'^\s*@Test')

    def parse(self, input_string: str) -> Tuple[List[str], List[str]]:
        lines = input_string.split('\n')
        comments, first_test_block = self._parse_comments_and_test(lines)

        tests_blob = '\n'.join(first_test_block)

        test_methods = self._parse_test_from_string(tests_blob)

        return comments, test_methods

    def _parse_test_from_string(self, content: str) -> List[str]:
        brace_count = 0
        test_methods = []
        extracted_test = []
        test_case_started = False
        lines = content.split('\n')

        for line in lines:
            if self.test_start_pattern.match(line):
                test_case_started = True
            if test_case_started:
                extracted_test.append(line)
                brace_count += line.count('{') - line.count('}')
                if brace_count == 0 and line.strip().endswith('}'):
                    test_case_started = False
                    test_methods.append('\n'.join(extracted_test))
                    extracted_test = []
        return test_methods

    def _parse_comments_and_test(self, lines: List[str]) -> Tuple[List[str], List[str]]:
        test_case_started = False
        test_method_ended = False
        extracted_test = []
        comments = []
        brace_count = 0

        for line in lines:
            if self.test_start_pattern.match(line):
                test_case_started = True
                test_method_ended = False

            if test_case_started and not test_method_ended:
                extracted_test.append(line)
                brace_count += line.count('{') - line.count('}')
                # Check if this line ends the test method
                if brace_count == 0 and '}' in line:
                    # Check if there's content after the closing brace
                    closing_brace_index = line.rfind('}')
                    content_after_brace = line[closing_brace_index + 1:].strip()

                    if content_after_brace:
                        # Split the line: part before and including '}' stays in test, rest becomes comment
                        test_part = line[:closing_brace_index + 1]
                        comment_part = content_after_brace

                        # Replace the last line in extracted_test with just the test part
                        extracted_test[-1] = test_part
                        extracted_test.append("\n")
                        test_method_ended = True

                        # Add the remaining part as a comment
                        if comment_part:
                            comments.append(f"// {comment_part}")
                    else:
                        # Normal case: line ends cleanly with '}'
                        extracted_test.append("\n")
                        test_method_ended = True
            else:
                # Comment out everything that's not part of a test method
                if line.strip():  # Only comment non-empty lines
                    comments.append(f"// {line}")
                else:
                    comments.append(line)  # Keep empty lines as they are
        return comments, extracted_test
