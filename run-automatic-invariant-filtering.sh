#!/bin/bash

# parameters
subject_class=$1
spec_file=$2
method_name=$3
test_suite=$4
test_driver=$5
class_name=$(basename "$subject_class" .java)

echo "==> Running automatic invariant filtering"

# create the output folder
output_dir="output/${class_name}_${method_name}"
mkdir -p "$output_dir"

# copy the existing test suite
cp "$test_suite" "${test_suite%.java}Augmented.java"
augmented_test_suite="${test_suite%.java}Augmented.java"
cp "$test_driver" "${test_driver%.java}Augmented.java"
augmented_test_driver="${test_driver%.java}Augmented.java"

# call the search-counterexample.py script, which will generate the tests and save them in the output folder
echo "> Generate tests using LLM"
python search-counterexample.py "$output_dir" "$subject_class" "$spec_file" "$method_name"
generated_test_file="$output_dir/test/${class_name}_${method_name}LlmTest.java"

# extract the generated tests
echo "> Extract the generated tests"

# fix the generated tests
echo "> Fix the generated tests"

# get the compilable test suite
echo "> Compile the test suite"

# append the generated tests by LLM to the existing test suite
echo "> Append the generated tests to the existing test suite"
python scripts/test_appender.py "$augmented_test_suite" "$augmented_test_driver" "$generated_test_file" "$subject_class"
