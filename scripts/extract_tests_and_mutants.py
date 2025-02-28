import sys
import re

test_and_mutants_file = sys.argv[1]

reading_test = False
reading_mutant = False

test_and_mutants = []

test = ""
mutant = ""

with open(test_and_mutants_file, 'r') as f:
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
                test_and_mutants.append((test, mutant))
                mutant = ""
                test = ""
            

for (t, m) in test_and_mutants:
    print(t)
    print(m)
