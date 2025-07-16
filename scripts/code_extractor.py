import re


def get_java_package_name(file_path: str) -> str:
    parts = file_path.split('/java/')
    if len(parts) > 1:
        result = parts[1].split('/')
        return ".".join(result[:-1]).replace('/', '.')
    return ""


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
