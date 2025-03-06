import sys
import os


def replace_line_of_file(file_path: str, line_number: int, new_line: str) -> str:
    """
    Replaces a specific line in a Java file while preserving indentation.

    :param file_path: Path to the Java file.
    :param line_number: Line number to replace (1-based index).
    :param new_line: New line content to insert.
    """
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if line number is valid
    if line_number < 1 or line_number > len(lines):
        raise IndexError("Line number out of range.")

    # Preserve indentation
    original_line = lines[line_number - 1]
    leading_whitespace = original_line[:len(
        original_line) - len(original_line.lstrip())]

    # Replace the specified line with preserved indentation
    lines[line_number - 1] = leading_whitespace + new_line + '\n'

    return lines


subject_name = sys.argv[1]
class_name = sys.argv[2]
mutant = sys.argv[3]
class_file = sys.argv[4]

mutated_line = int(mutant.split(":", 1)[0].strip())
mutation = mutant.split(":", 1)[1].strip()

new_lines = replace_line_of_file(class_file, mutated_line, mutation)

os.remove(class_file)

with open(class_file, 'w') as f:
    f.writelines(new_lines)
