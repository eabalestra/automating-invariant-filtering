import re


def append_test_method_to_file(destination_file: str, test_method: str) -> None:
    try:
        with open(destination_file, 'r+', encoding='utf-8') as df:
            content = df.read()
            if '}' not in content:
                print("No closing brace '}' found in the existing test file.")
                return
            head, tail = content.rsplit('}', 1)
            new_content = f"{head}\n{test_method}\n}}{tail}"
            df.seek(0)
            df.write(new_content)
            df.truncate()
    except IOError as e:
        print(f'Error processing file {destination_file}: {e}')


def extract_package_path(file_path: str) -> str:
    parts = file_path.split('/java/')
    if len(parts) > 1:
        result = parts[1].split('/')
        return ".".join(result[:-1]).replace('/', '.')


def extract_method_code(class_code: str, method_name: str) -> str:
    pattern = r'^\s*(?:(?:public)|(?:private)|(?:static)|(?:protected)\s+)*.*\s+' + \
        method_name + r'\s*\(.*\)\s*(?:throws\s+[\w\s,]+)?\s*{'

    match = re.search(pattern, class_code, re.MULTILINE)
    if not match:
        return ""

    start_index = match.start()
    brace_count = 0
    end_index = start_index

    for i in range(start_index, len(class_code)):
        if class_code[i] == '{':
            brace_count += 1
        elif class_code[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_index = i + 1
                break

    return class_code[start_index:end_index]


def extract_class_name(class_code):
    pattern = r'public\s+class\s+(\w+)'
    match = re.search(pattern, class_code)
    if not match:
        raise ValueError("Class name not found in the provided class code.")
    return match.group(1)
