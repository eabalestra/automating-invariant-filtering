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

# Find the files
subject_sources="$SUBJECTS_DIR/$subject_name"
class_path=$(find "$subject_sources/src/main/java" -type f -name "$class_name".java)
assertions_file="$SPECS_DIR/$subject_name/output/$class_name-$method_name-specfuzzer-1.assertions"
invs_by_mutants="$SPECS_DIR/$subject_name/output/$class_name-$method_name-specfuzzer-1-invs-by-mutants.csv"
test_suite=$(find "$subject_sources/src/test/java" -type f -name "$test_suite_name".java)
test_driver=$(find "$SUBJECTS_DIR/$subject_name/src/test/java" -type f -name "$test_driver_name".java)
build_dir=$subject_sources/build
subject_cp="$build_dir/libs/*"
cp_for_daikon="libs/*:$subject_cp"

# Remove the word driver from test_suite_driver_name
driver_base=${test_driver_name%Driver}
driver_base=${driver_base%DriverAugmented}
assertions_file_name=$(basename "${assertions_file%.*}")

echo "=> Running mutation-based invariant filtering"
echo "> Class: $class_name"
echo "> Method: $method_name"
echo "> Test suite: $test_suite_name"
echo "> Test driver: $test_driver_name"
echo ""

# Create the output directory
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

# generate mutants using LLM
echo '> Generating mutants using LLM'
python3 search-mutant.py "$class_path" "$method_name" "$non_mutant_killing_assertions_file" "$mutants_dir"
generated_mutants=$mutants_dir/llm/${class_name}_${method_name}LlmGeneratedMutants.txt
echo ''

# extract the mutations from the generated response and write the mutations to a file
python3 scripts/extract_tests_and_mutants.py "$generated_mutants" "$mutants_dir/generated-mutations.txt" "$class_path"
[ -f "$mutants_dir/compiled-mutations.txt" ] && rm "$mutants_dir/compiled-mutations.txt"

cat $mutants_dir/generated-mutations.txt | sed 's/`//g' | awk '!seen[$0]++' >"$mutants_dir/temp-mutations.txt" && mv "$mutants_dir/temp-mutations.txt" "$mutants_dir/generated-mutations.txt"

# backup the original class
cp "$class_path" "$mutants_dir"

# apply the mutations
i=0
echo '> Applying mutations'
while IFS= read -r mutant; do
    echo ": Mutant: $mutant"
    python3 scripts/mutate-code.py "$subject_name" "$class_name" "$mutant" "$class_path"
    mutant_dir="$mutants_dir"/mutants/${i}
    mkdir -p "$mutant_dir"
    mv "$class_path" "$mutant_dir"/"$class_name".java

    # generate test files for the mutant
    python3 scripts/generate_mutant_test_files.py "$mutant" mutant_tests.csv "$test_suite" "$test_driver" "$mutant_dir" $i

    # compile files
    javac -cp $build_dir/libs/* -g "$mutant_dir/$class_name.java" -d $build_dir >/dev/null 2>&1
    javac -cp "libs/junit-4.12.jar:$subject_cp:$build_dir" -d "$build_dir" "$mutant_dir/${test_suite_name}Mutant${i}.java"
    javac -cp "libs/junit-4.12.jar:$subject_cp:$build_dir" -d "$build_dir" "$mutant_dir/${test_driver_name}Mutant${i}.java"

    if [ $? -ne 0 ]; then
        rm -rf "$mutant_dir"
    else
        echo "$mutant" >>"$mutants_dir/compiled-mutations.txt"
        i=$((i + 1))
    fi
    cp "$mutants_dir/$class_name.java" "$class_path"
done <"$mutants_dir/generated-mutations.txt"
echo ''

# restore the original class
rm "$class_path"
mv "$mutants_dir/$class_name.java" "$class_path"

# remove csv file
rm -f mutant_tests.csv

# TODO: generate dynamic comparability file for each mutant driver and generate traces
echo '> Processing mutants'
for dir in $mutants_dir/mutants/*/; do
    target_file=$(basename "$class_path")
    dir2=${dir%*/}
    number=${dir2##*/}
    driver_fqname="testers.${test_driver_name}Mutant${number}"
    echo '> Processing mutant: '$dir$target_file
    echo '> Compiling mutant'
    javac -cp $build_dir/libs/* -g $dir$target_file -d $build_dir
    echo '> Mutant compiled'
    echo "> Performing Dynamic Comparability Analysis from driver: ${driver_fqname}"
    java -cp "$cp_for_daikon" daikon.DynComp "$driver_fqname"
    echo '> Generating traces with Chicory from mutant'
    java -cp $cp_for_daikon daikon.Chicory --output-dir=daikon-outputs/mutants --comparability-file=$daikon_output_folder/$test_suite_driver_name'.decls-DynComp' --ppt-omit-pattern=$driver_base'.*' --ppt-omit-pattern='org.junit.*' --dtrace-file=$test_suite_driver_name'-llm-m'$number'.dtrace.gz' testers.$test_suite_driver_name daikon-outputs/mutants/$test_suite_driver_name'-llm-m'$number'-objects.xml' >/dev/null 2>&1
    echo ''
done

# Move the whole mutants folder to the output folder
mkdir -p $mutants_dir/mutants-traces
rm -rf $mutants_dir/mutants-traces/*
mv daikon-outputs/mutants/$driver_base* $mutants_dir/mutants-traces/
rm -rf daikon-outputs

echo '> Done'
echo ''
