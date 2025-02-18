def read_file(file_path: str, mode: str = 'r') -> str:
    with open(file_path, mode, encoding='utf-8') as f:
        return f.read()


def write_file(file_path: str, content: str, mode: str) -> None:
    with open(file_path, mode, encoding='utf-8') as f:
        f.write(content)
