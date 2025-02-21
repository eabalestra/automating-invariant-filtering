import sys
import os

def replace_line_of_file(file_path, line_number, new_line):
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
    leading_whitespace = original_line[:len(original_line) - len(original_line.lstrip())]
    
    # Replace the specified line with preserved indentation
    lines[line_number - 1] = leading_whitespace + new_line + '\n'
    
    return lines

subjects_dir = os.getenv("SUBJECTS_DIR")
if not subjects_dir:
    raise ValueError("SUBJECTS_DIR should be set")

subject_name = sys.argv[1]
class_name = sys.argv[2]
mutant = sys.argv[3]
mutated_line = int(mutant.split(":")[0].strip())
mutation = mutant.split(":")[1].strip()

orig_file_path = f"{subjects_dir}/{subject_name}/orig/{class_name}.java"
new_lines = replace_line_of_file(orig_file_path, mutated_line, mutation)

for line in new_lines:
    print(line, end='')
