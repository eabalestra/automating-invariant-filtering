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
    method_started = False
    method = []
    brace_count = 0

    for line in class_code.split('\n'):
        if method_name in line:
            method_started = True
        if method_started:
            method.append(line)
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and line.strip().endswith('}'):
                method_started = False
    return '\n'.join(method)


def extract_class_name(class_code):
    pattern = r'public\s+class\s+(\w+)'
    match = re.search(pattern, class_code) 
    if not match:
        raise ValueError("Class name not found in the provided class code.")
    return match.group(1)
