import os
import sys
import re

from test_extractor import extract_tests_from_file

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_test_suite> <output_dir>")
        sys.exit(1)

    source_test_suite = sys.argv[1]
    output_dir = sys.argv[2]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    tests = extract_tests_from_file(source_test_suite)

    for test in tests:

        test_name_match = re.search(r'public void (\w+)\(', test)
        if test_name_match:
            test_name = test_name_match.group(1)
        else:
            test_name = f"unknown_test_{hash(test) % 10000}"

        test_path = os.path.join(output_dir, f"{test_name}.txt")
        with open(test_path, "w") as file:
            file.write(test + "\n")
