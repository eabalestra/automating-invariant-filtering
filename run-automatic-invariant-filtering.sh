#!/bin/bash
source scripts/init_env.sh
source venv/bin/activate

# parameters
subject_name=$1
class_name=$2
method_name=$3
class_path=$(find "$SUBJECTS_DIR/$subject_name/src/main/java" -type f -name "$class_name".java)
spec_file="$SPECS_DIR/$subject_name/output/$class_name-$method_name-specfuzzer-1.assertions"
test_suite_name=$4
test_suite=$(find "$SUBJECTS_DIR/$subject_name/src/test/java" -type f -name "$test_suite_name".java)
test_driver_name=$5
test_driver=$(find "$SUBJECTS_DIR/$subject_name/src/test/java" -type f -name "$test_driver_name".java)

echo "==> Running automatic invariant filtering"
echo "Class: $(basename "$class_path")"
echo "Spec file: $(basename "$spec_file")"
echo "Test suite: $(basename "$test_suite")"
echo "Test driver: $(basename "$test_driver")"

# create the output folder
output_dir="output/${class_name}_${method_name}"
mkdir -p "$output_dir"

log_file="$output_dir/${class_name}_${method_name}.log"

# copy the existing test suite
augmented_test_suite="${test_suite%.java}Augmented.java"
cp "$test_suite" "$augmented_test_suite"
augmented_test_driver="${test_driver%.java}Augmented.java"
cp "$test_driver" "$augmented_test_driver"

# generate tests using LLM
echo "> Generate tests using LLM"
python search-counterexample.py "$output_dir" "$class_path" "$spec_file" "$method_name"
tests_output_dir="$output_dir/test"
llm_generated_test_suite="$tests_output_dir/${class_name}_${method_name}LlmTest.java"

echo "> Prepare destination for the generated tests"
name_suffix="Augmented"
python scripts/prepare_destination_test_files.py "$augmented_test_suite" "$augmented_test_driver" $name_suffix

# fix the generated tests
echo "> Fix the generated tests"
python scripts/fix_llm_tests.py "$tests_output_dir" "$llm_generated_test_suite" "$class_path" "$method_name"
llm_fixed_test_suite="$tests_output_dir/${class_name}_${method_name}LlmFixedTest.java"

# get the compilable test suite
echo "> Compile the test suite"
python scripts/discard_uncompilable_llm_tests.py "$tests_output_dir" "$augmented_test_suite" "$class_path" "$llm_fixed_test_suite" "$method_name"
llm_compilable_test_suite="$tests_output_dir/${class_name}_${method_name}LlmCompilableTest.java"

# append the generated tests by LLM to the existing test suite
echo "> Append the generated tests to the existing test suite"
python scripts/append_llm_tests.py "$augmented_test_suite" "$augmented_test_driver" "$llm_compilable_test_suite" "$class_path"

echo "> Done"
echo "Output is saved in $output_dir"
echo "Log is saved in $log_file"
