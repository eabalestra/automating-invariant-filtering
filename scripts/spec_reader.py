from re import search


def is_inv_line(line: str) -> bool:
    return not (search(":::OBJECT", line) or search("==============", line) or search(":::POSTCONDITION", line) or search(":::ENTER", line) or search("buckets=", line) or search("specs=", line))


def read_and_filter_specs(file_path: str) -> set:
    specs = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
        for line in lines:
            if is_inv_line(line):
                specs.append(line)
    return set(specs)
