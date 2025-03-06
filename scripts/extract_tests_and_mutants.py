import sys
import re

import pandas as pd

from fix_llm_tests import add_test_signatures, add_throws_declaration, rename_test_methods, replace_class_references

tests_and_mutants_file = sys.argv[1]
output_mutation = sys.argv[2]
class_file = sys.argv[3]

reading_test = False
reading_mutant = False

tests = []
mutants = []

test = ""
mutant = ""

with open(tests_and_mutants_file, 'r') as f:
    brace_count = 0
    test_start_pattern = re.compile(r'^\s*@Test')
    for line in f.readlines():
        if "[[TEST]]" in line or test_start_pattern.match(line):
            reading_test = True
            reading_mutant = False
            continue
        if "[[MUTATION]]" in line:
            reading_test = False
            reading_mutant = True
            continue

        if reading_test:
            test += line
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and line.strip().endswith('}'):
                test_case_started = False
                if test != "":
                    tests.append(test)
                test = ""

        if reading_mutant:
            # if re.match(r'\d+:.+', line):
            if re.match(r'\d+:.*[;:{}()]', line):
                mutant += line
            else:
                reading_mutant = False
                if test != "":
                    tests.append(test.replace("`", ""))
                if mutant != "":
                    mutants.append(mutant.replace("`", ""))
                mutant = ""
                test = ""


tests = rename_test_methods(tests, 'llmMutationTest')
tests = replace_class_references(tests, class_file)
tests = add_throws_declaration(tests)
tests = add_test_signatures(tests)

tests_and_mutants = list(zip(tests, mutants))

tests_with_mutants_df = pd.DataFrame(
    tests_and_mutants, columns=["test", "mutant"])

tests_with_mutants_df.to_csv("mutant_tests.csv", index=False)

with open(output_mutation, 'w') as mutants_file:
    for m in tests_with_mutants_df["mutant"].unique():
        mutants_file.write(m)
