import sys
import re

tests_and_mutants_file = sys.argv[1]
output_mutation = sys.argv[2]

reading_test = False
reading_mutant = False

tests_and_mutants = []

test = ""
mutant = ""

with open(tests_and_mutants_file, 'r') as f:
    for line in f.readlines():
        if "[[TEST]]" in line:
            reading_test = True
            reading_mutant = False
            mutant = ""
            continue
        if "[[MUTATION]]" in line:
            reading_test = False
            reading_mutant = True
            continue
        
        if reading_test:
            test += line

        if reading_mutant:
            if re.match(r'\d+:.+', line):
                mutant += line
            else:
                reading_mutant = False
                tests_and_mutants.append((test, mutant))
                mutant = ""
                test = ""
            
with open(output_mutation, 'w') as mutants_file:
    for (t, m) in tests_and_mutants:
        print(t)
        mutants_file.write(m)
