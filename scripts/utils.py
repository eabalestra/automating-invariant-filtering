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
