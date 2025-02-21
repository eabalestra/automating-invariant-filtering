def replace_line_in_file(file_path, line_number, new_line):
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

file_path = sys.argv[1]  # Change to your Java file path
line_number = sys.argv[2]  # Line to replace
new_line = sys.argv[3]  # New line content

new_lines = replace_line_of_file(file_path, line_number, new_line)

for line in new_lines:
    print(line)
