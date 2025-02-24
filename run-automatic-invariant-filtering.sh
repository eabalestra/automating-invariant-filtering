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

log_file="$output_dir/${class_name}_${method_name}.log"

# copy the existing test suite
cp "$test_suite" "${test_suite%.java}Augmented.java"
augmented_test_suite="${test_suite%.java}Augmented.java"
cp "$test_driver" "${test_driver%.java}Augmented.java"
augmented_test_driver="${test_driver%.java}Augmented.java"

# generate tests using LLM
echo "> Generate tests using LLM"
python search-counterexample.py "$output_dir" "$subject_class" "$spec_file" "$method_name" >>"$log_file"
tests_output_dir="$output_dir/test"
llm_generated_test_suite="$tests_output_dir/${class_name}_${method_name}LlmTest.java"

echo "> Prepare destination for the generated tests"
python scripts/prepare_destination_test_files.py "$augmented_test_suite" "$augmented_test_driver" >>"$log_file"

# fix the generated tests
echo "> Fix the generated tests"
python scripts/fix_llm_tests.py "$tests_output_dir" "$llm_generated_test_suite" "$subject_class" "$method_name" >>"$log_file"
llm_fixed_test_suite="$tests_output_dir/${class_name}_${method_name}LlmFixedTest.java"

# get the compilable test suite
echo "> Compile the test suite"
python scripts/discard_uncompilable_llm_tests.py "$tests_output_dir" "$augmented_test_suite" "$subject_class" "$llm_fixed_test_suite" "$method_name" >>"$log_file"
llm_compilable_test_suite="$tests_output_dir/${class_name}_${method_name}LlmCompilableTest.java"

# append the generated tests by LLM to the existing test suite
echo "> Append the generated tests to the existing test suite"
python scripts/append_llm_tests.py "$augmented_test_suite" "$augmented_test_driver" "$llm_compilable_test_suite" "$subject_class" >>"$log_file"

echo "> Done"
echo "Output is saved in $output_dir"
echo "Log is saved in $log_file"
