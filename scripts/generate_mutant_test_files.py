import os
import sys
import pandas as pd

from prepare_destination_test_files import rename_classes_in_file
from append_llm_tests import add_generated_tests_to_suite, append_tests_into_driver_file, extract_test_names

mutant = sys.argv[1].strip()
test_and_mutants_csv = sys.argv[2]
original_test_suite = sys.argv[3]
original_test_driver = sys.argv[4]
output_dir = sys.argv[5]
mutant_number = sys.argv[6]

original_suite_name = os.path.basename(
    original_test_suite).replace(".java", "")
original_driver_name = os.path.basename(
    original_test_driver).replace(".java", "")


def copy_suite(test_suite: str) -> str:
    test_header = ""
    with open(test_suite, "r") as f:
        lines = f.readlines()

    for line in lines:
        test_header += line
        if "{" in line:
            test_header += "\n}"
            break
    return test_header


def copy_driver(test_driver: str) -> str:
    test_header = ""
    with open(test_driver, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "new" in line:
            line = line.replace(f"{original_suite_name} ",
                                f"{original_suite_name}Mutant{mutant_number} ")
            line = line.replace(
                f"new {original_suite_name}(", f"new {original_suite_name}Mutant{mutant_number}(")
            test_header += line
            test_header += "        if (hadFailure) { \n            System.exit(1);\n        }"
            test_header += "\n    }\n}"
            break
        test_header += line
    return test_header


try:
    df = pd.read_csv(test_and_mutants_csv)
except Exception as e:
    print("Error reading CSV file: ", e)
    sys.exit(1)

if "mutant" not in df.columns:
    sys.exit(1)

# delete leading and trailing whitespaces
df["mutant"] = df["mutant"].astype(str).str.strip()

# find the rows with the mutant
mutant_rows = df[df["mutant"] == mutant]

if mutant_rows.empty:
    sys.exit(1)

tests_to_write = mutant_rows["test"].dropna().tolist()

test_suite = copy_suite(original_test_suite)
output_suite = os.path.join(
    output_dir, f"{original_suite_name}Mutant{mutant_number}.java")
open(output_suite, "w").write(test_suite)

test_driver = copy_driver(original_test_driver)
output_driver = os.path.join(
    output_dir, f"{original_driver_name}Mutant{mutant_number}.java")
open(output_driver, "w").write(test_driver)

rename_classes_in_file(output_suite, f"Mutant{mutant_number}")
rename_classes_in_file(output_driver, f"Mutant{mutant_number}")

add_generated_tests_to_suite(output_suite, tests_to_write)
tests_to_write_names = extract_test_names(tests_to_write)

append_tests_into_driver_file(output_driver, tests_to_write_names)
