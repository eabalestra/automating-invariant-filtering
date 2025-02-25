#!/bin/bash
source scripts/init_env.sh

# Arguments
subject_name="$1"
target_class_fqname="$2"
method_name="$3"
test_suite_name="$4"

# Find the files
class_name="${target_class_fqname##*.}"
class_path=$(find "$SUBJECTS_DIR/$subject_name/src/main/java" -type f -name "$class_name".java)
assertions_file="$SPECS_DIR/$subject_name/output/$class_name-$method_name-specfuzzer-1.assertions"
invs_by_mutants="$SPECS_DIR/$subject_name/output/$class_name-$method_name-specfuzzer-1-invs-by-mutants.csv"
test_suite=$(find "$SUBJECTS_DIR/$subject_name/src/test/java" -type f -name "$test_suite_name".java)

assertions_file_name=$(basename "${assertions_file%.*}")

echo "=> Running mutation-based invariant filtering"
echo "> Class: $class_name"
echo "> Method: $method_name"
echo "> Test suite: $test_suite_name"

# Create the output directory
automating_if_subject_dir="output/${class_name}_${method_name}"
assertions_dir="$automating_if_subject_dir/specs"
mutants_dir="$automating_if_subject_dir/mutations"
mkdir -p "$assertions_dir"
mkdir -p "$mutants_dir/mutants"

# Get the non-mutant killing assertions
python scripts/compute-non-mutants-killing-specs.py "$assertions_file" "$invs_by_mutants" "$class_name" "$method_name"
non_mutant_killing_assertions_file="$assertions_dir/${assertions_file_name}-non-mutant-killing.assertions"

# generate mutants using LLM
python search-mutant.py "$class_path" "$method_name" "$test_suite" "$non_mutant_killing_assertions_file" "$mutants_dir"
generated_mutants=$mutants_dir/llm/${class_name}_${method_name}LlmGeneratedMutants.txt

# extract the mutations from the generated response
mutations=$(grep -o '[0-9]\+:.*[;:{}()]' "$generated_mutants" | sed 's/`//g' | awk '!seen[$0]++')

# write the mutations to a file
echo "$mutations" >"$mutants_dir/mutations.txt"

# backup the original class
cp "$class_path" "$mutants_dir"

# apply the mutations
i=0
while IFS= read -r mutant; do
    python scripts/mutate-code.py "$subject_name" "$class_name" "$mutant" "$class_path" "$mutants_dir"
    cp "$class_path" "$mutants_dir"/mutants/"$class_name"-${i}.java
    i=$((i + 1))
done <"$mutants_dir/mutations.txt"

# restore the original class
rm "$class_path"
mv "$mutants_dir/$class_name.java" "$class_path"
