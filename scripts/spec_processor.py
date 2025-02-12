import re

def strip_outer_parentheses(expr):
    expr = expr.strip()
    if expr.startswith('(') and expr.endswith(')'):
        depth = 0
        for i, ch in enumerate(expr):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if depth == 0 and i < len(expr) - 1:
                return expr
        return expr[1:-1].strip()
    return expr

def split_outside_parentheses(spec, op_regex, max_splits=1):
    parts = []
    current = []
    depth = 0
    splits = 0
    i = 0
    while i < len(spec):
        char = spec[i]
        if char == '(':
            depth += 1
            current.append(char)
            i += 1
        elif char == ')':
            depth -= 1
            current.append(char)
            i += 1
        else:
            if depth == 0:
                m = re.match(op_regex, spec[i:], re.IGNORECASE)
                if m:
                    parts.append(''.join(current).strip())
                    current = []
                    i += m.end()
                    splits += 1
                    if splits == max_splits:
                        current.append(spec[i:])
                        break
                    continue
                else:
                    current.append(char)
                    i += 1
            else:
                current.append(char)
                i += 1
    parts.append(''.join(current).strip())
    return parts

def replace_spec_variables(specification):
    processed_spec = specification.replace("FuzzedInvariant", "").strip()
    if "holds for:" in processed_spec:
        processed_spec, vars_part = processed_spec.split("holds for:")
        processed_spec = processed_spec.strip()
        variable_names = vars_part.strip().strip("<>").split(",")

        quantified_pattern = re.compile(r'\b(?:some|all|no)\s+n\b', re.IGNORECASE)
        if quantified_pattern.search(processed_spec):
            variable_names = variable_names[1:]

        for var in variable_names:
            # if var.startswith("orig("):
            #     var = var.replace("orig(", "").replace(")", "")
            match = re.search(r'\w+_Variable_\d+', processed_spec)
            if match:
                processed_spec = processed_spec.replace(match.group(0), var.strip())
    processed_spec = processed_spec.replace("\\", "")
    return strip_outer_parentheses(processed_spec).strip()

def normalize_spec(specification):
    specification = specification.replace(" or ", " || ").replace("and", "&&").replace("not", "!").strip()
    spec = strip_outer_parentheses(specification.strip())
    parts = split_outside_parentheses(spec, r'\s*xor\s*', max_splits=1)
    if len(parts) > 1:
        first = normalize_spec(parts[0])
        second = normalize_spec(parts[1])
        return f'(!({first} && {second}) && ({first} || {second}))'
    parts = split_outside_parentheses(spec, r'\s*(implies|==>)\s*', max_splits=1)
    if len(parts) > 1:
        first = normalize_spec(parts[0])
        second = normalize_spec(parts[1])
        return f'!({first}) || ({second})'
    parts = split_outside_parentheses(spec, r'\s*(iff|<=>)\s*', max_splits=1)
    if len(parts) > 1:
        first = normalize_spec(parts[0])
        second = normalize_spec(parts[1])
        return f'({first}) == ({second})'
    return spec
