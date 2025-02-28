import re

def extract_class_attributes_and_method(file_path, method_name):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    filtered_lines = []
    inside_method = False
    inside_class = False
    method_pattern = re.compile(rf'\b{re.escape(method_name)}\b\s*\(')
    open_braces = 0
    m_open_braces = 0
    class_signature_found = False
    mut_signature_found = False
    method_signature_found = False
    
    i = 0
    for line in lines:
        i = i + 1
        
        if re.match(r'^\s*$', line):
            continue
        if re.match(r'(\s|\t)*(//|/\*|\*|package|import").*', line):
            continue

        # Detect class start (handle cases where { is on a separate line)
        if not inside_class and re.match(r'(\s|\t)*(public|private|protected)?\s*(class|interface)\s+\w+', line):
            class_signature_found = True
            filtered_lines.append(f"{i:3} {line}")
            inside_class = False
        
        if class_signature_found and "{" in line:
            inside_class = True
            class_signature_found = False
        
        # Track class scope
        if inside_class:
            open_braces += line.count("{")
            open_braces -= line.count("}")
            if open_braces == 0:
                filtered_lines.append(f"{i:3} {line}")
                inside_class = False

        if inside_class:
            if method_pattern.search(line):
                mut_signature_found = True
                inside_method = False

            if re.match(r'(\s|\t)*(public|private|protected)(\s+\w+)+\(.*', line):
                method_signature_found = True
                inside_method = False

            if (mut_signature_found or method_signature_found) and "{" in line:
                inside_method = True

            if not (inside_method or method_signature_found or mut_signature_found):
                if re.match(r'(\s|\t)*(private|protected|public)?\s*(static\s+|final\s+)*\w+(\[\])?\s+\w+\s*(=\s*[^;]+)?;', line):
                    filtered_lines.append(f"{i:3} {line}")
            
            if inside_method and mut_signature_found:
                filtered_lines.append(f"{i:3} {line}")

            if inside_method:
                m_open_braces += line.count("{")
                m_open_braces -= line.count("}")
                if m_open_braces == 0:
                    inside_method = False
                    mut_signature_found = False
                    method_signature_found = False
                
    return "".join(filtered_lines)
