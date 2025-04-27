import re
from typing import List


def strip_outer_parentheses(spec: str) -> str:
    spec = spec.strip()
    if spec.startswith('(') and spec.endswith(')'):
        depth = 0
        for i, ch in enumerate(spec):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if depth == 0 and i < len(spec) - 1:
                return spec
        return spec[1:-1].strip()
    return spec


def split_by_operator_outside_parens(spec: str, op_regex: re.Pattern, max_splits: int = 1) -> List[str]:
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
                regex_match = re.match(op_regex, spec[i:], re.IGNORECASE)
                if regex_match:
                    parts.append(''.join(current).strip())
                    current = []
                    i += regex_match.end()
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


def update_specification_variables(specification: str, class_name: str) -> str:
    processed_spec = specification.replace("FuzzedInvariant", "").strip()

    if "holds for:" in processed_spec:
        processed_spec, vars_section = processed_spec.split("holds for:")
        processed_spec = processed_spec.strip()
        variable_names = vars_section.strip().strip("<>").split(",")

        quantified_pattern = re.compile(
            r'\b(?:some|all|no)\s+n\b', re.IGNORECASE)
        if quantified_pattern.search(processed_spec):
            variable_names = variable_names[1:]

        variable_iter = iter(variable_names)
        for var in variable_iter:
            if (var == "this" or var == "orig(this)") and class_name in specification:
                processed_spec = processed_spec.replace(class_name, var)
                var = next(variable_iter, var)
            match = re.search(r'\w+_Variable_\d+', processed_spec)
            if match:
                processed_spec = processed_spec.replace(
                    match.group(0), var.strip())

    processed_spec = processed_spec.replace("daikon.Quant.", "")
    processed_spec = processed_spec.replace("orig(", r"\old(")
    processed_spec = processed_spec.replace("\\", "")
    return strip_outer_parentheses(processed_spec).strip()


def transform_specification(specification: str) -> str:
    specification = specification.replace(" or ", " || ").replace(
        "and", "&&").replace("not", "!").strip()

    spec = strip_outer_parentheses(specification.strip())

    xor_regex = r'\s*xor\s*'
    if_regex = r'\s*(implies|==>)\s*'
    iff_regex = r'\s*(iff|<=>)\s*'

    parts = split_by_operator_outside_parens(spec, xor_regex, max_splits=1)
    if len(parts) > 1:
        first = transform_specification(parts[0])
        second = transform_specification(parts[1])
        return f'(!({first} && {second}) && ({first} || {second}))'

    parts = split_by_operator_outside_parens(
        spec, if_regex, max_splits=1)
    if len(parts) > 1:
        first = transform_specification(parts[0])
        second = transform_specification(parts[1])
        return f'!({first}) || ({second})'

    parts = split_by_operator_outside_parens(
        spec, iff_regex, max_splits=1)
    if len(parts) > 1:
        first = transform_specification(parts[0])
        second = transform_specification(parts[1])
        return f'({first}) == ({second})'

    return spec
