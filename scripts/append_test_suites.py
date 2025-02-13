import sys

def append_generated_tests(existing_test_file, generated_test_file):
    with open(generated_test_file, encoding='utf-8') as gf:
        generated = gf.read()
    with open(existing_test_file, 'r+', encoding='utf-8') as ef:
        content = ef.read()
        if '}' not in content:
            print("No closing brace '}' found in the existing test file.")
            return
        head, tail = content.rsplit('}', 1)
        new_content = f"{head}\n{generated}\n}}{tail}"
        ef.seek(0)
        ef.write(new_content)
        ef.truncate()
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python scripts/append_test_suites.py <existing_test_file> <generated_test_file>")
    append_generated_tests(sys.argv[1], sys.argv[2])
    