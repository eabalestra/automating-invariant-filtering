#!/bin/bash
source scripts/init_env.sh
source venv/bin/activate

# Arguments
subject_name="$1"
target_class_fqname="$2"
method_name="$3"
test_suite_name="$4"
test_driver_name="$5"
class_name="${target_class_fqname##*.}"

# Set subject root directory
subject_root="$SUBJECTS_DIR/$subject_name"

# Find the files
class_path=$(find "$subject_root/src/main/java" -type f -name "$class_name".java)
assertions_file="$SPECS_DIR/$subject_name/output/${class_name}-${method_name}-specfuzzer-1.assertions"
invs_by_mutants="$SPECS_DIR/$subject_name/output/${class_name}-${method_name}-specfuzzer-1-invs-by-mutants.csv"
test_suite=$(find "$subject_root/src/test/java" -type f -name "$test_suite_name".java)
test_driver=$(find "$subject_root/src/test/java" -type f -name "$test_driver_name".java)

# Find the build file by traversing upward from the class file location
build_file_dir=""
current_dir="$class_path"
while [ "$current_dir" != "/" ]; do
    build_file=$(find "$current_dir" -maxdepth 1 \( -name "build.gradle" -o -name "pom.xml" \) | head -n 1)
    if [ -n "$build_file" ]; then
        build_file_dir="$build_file"
        break
    fi
    current_dir=$(dirname "$current_dir")
done
if [ -z "$build_file_dir" ]; then
    echo "Build file not found"
    exit 1
fi

# Use the build file directory as the subject's build directory
subject_build_dir=$(dirname "$build_file_dir")
subject_cp="$subject_build_dir/build/libs/*"

# Prepare classpath for Daikon
cp_for_daikon="libs/*:$subject_cp"

# Remove the word driver from test_driver_name
driver_base=${test_driver_name%Driver}
driver_base=${driver_base%DriverAugmented}
assertions_file_name=$(basename "${assertions_file%.*}")

echo "=> Running mutation-based invariant filtering"
echo "> Class: $class_name"
echo "> Method: $method_name"
echo "> Test suite: $test_suite_name"
echo "> Test driver: $test_driver_name"
echo ""

# Create the output directories
automating_if_subject_dir="output/${class_name}_${method_name}"
assertions_dir="$automating_if_subject_dir/specs"
mutants_dir="$automating_if_subject_dir/mutations"
daikon_output_folder="$automating_if_subject_dir/daikon"
mkdir -p "$assertions_dir"
mkdir -p "$mutants_dir/mutants"

# Get the non-mutant killing assertions
echo "> Computing non-mutant killing assertions"
python3 scripts/compute-non-mutants-killing-specs.py "$assertions_file" "$invs_by_mutants" "$class_name" "$method_name"
non_mutant_killing_assertions_file="$assertions_dir/${assertions_file_name}-non-mutant-killing.assertions"
echo ''

# Generate mutants using LLM
echo '> Generating mutants using LLM'
python3 search-mutant.py "$class_path" "$method_name" "$non_mutant_killing_assertions_file" "$mutants_dir"
generated_mutants="$mutants_dir/llm/${class_name}_${method_name}LlmGeneratedMutants.txt"
echo ''

# Extract the mutations from the generated response and write them to a file
python3 scripts/extract_tests_and_mutants.py "$generated_mutants" "$mutants_dir/generated-mutations.txt" "$class_path"
[ -f "$mutants_dir/compiled-mutations.txt" ] && rm "$mutants_dir/compiled-mutations.txt"
echo ''

cat "$mutants_dir/generated-mutations.txt" | sed 's/`//g' | awk '!seen[$0]++' >"$mutants_dir/temp-mutations.txt" && mv "$mutants_dir/temp-mutations.txt" "$mutants_dir/generated-mutations.txt"

# Backup the original class
cp "$class_path" "$mutants_dir/$class_name.java"

# Apply the mutations
i=0
echo '> Applying mutations'
while IFS= read -r mutant; do
    echo "> Processing mutant: $mutant"
    python3 scripts/mutate-code.py "$subject_name" "$class_name" "$mutant" "$class_path"
    mutant_dir="$mutants_dir/mutants/${i}"
    mkdir -p "$mutant_dir"

    # Generate test files for the mutant
    python3 scripts/generate_mutant_test_files.py "$mutant" mutant_tests.csv "$test_suite" "$test_driver" "$mutant_dir" "$i"

    # Recompile the subject (capture the exit code without stopping on failure)
    echo '> Compiling mutant'
    current_dir=$(pwd)
    cd "$subject_build_dir" || exit
    ./gradlew -q -Dskip.tests jar </dev/null
    build_status=$?
    cd "$current_dir" || exit

    if [ "$build_status" -ne 0 ]; then
        rm -rf "$mutant_dir"
    else
        echo "$mutant" >>"${mutants_dir}/compiled-mutations.txt"
        i=$((i + 1))
    fi

    echo '> Performing Dynamic Comparability Analysis from driver:'
    # TODO

    echo '> Generating traces with Chicory from mutant'
    # TODO

    # Move the mutant class file to the mutant directory
    mv "$class_path" "$mutant_dir/$class_name.java"
    # Restore the original class file for the next iteration
    cp "$mutants_dir/$class_name.java" "$class_path"
    echo ''

done <"$mutants_dir/generated-mutations.txt"
echo ''

# Restore the original class at the end
rm "$class_path"
mv "$mutants_dir/$class_name.java" "$class_path"

# Remove temporary CSV file
rm -f mutant_tests.csv

echo '> Done'
