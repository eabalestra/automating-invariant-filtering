#!/bin/bash

# shellcheck source=config/setup_env.sh disable=SC1091
source config/setup_env.sh

# shellcheck source=venv/bin/activate disable=SC1091
source venv/bin/activate

[ -z "$DAIKONDIR" ] && {
    echo "> The environment variable DAIKONDIR is not set"
    exit 1
}

# Arguments
subject_name=$1
target_class_fqname="$2"
class_name="${target_class_fqname##*.}"
target_class=$(find "$SUBJECTS_DIR/$subject_name/src/main/java" -type f -name "$class_name".java)
method="$3"
# TODO: this invs file is the same after bucketing?
specfuzzer_invs_file="$SPECS_DIR/$subject_name/output/$class_name-$method-specfuzzer-1.inv.gz"
specfuzzer_assertions_file="$SPECS_DIR/$subject_name/output/$class_name-$method-specfuzzer-1-buckets.assertions"

test_class_name="${class_name}Tester"
driver_name="${test_class_name}Driver"
test_suite_driver="${driver_name}Augmented"
driver_fqname="testers.${test_suite_driver}"

# Output files
OUTPUT_FOLDER="output"
output_dir="$OUTPUT_FOLDER/${class_name}_${method}"
daikon_output_folder="$output_dir/daikon"
specs_output_folder="$output_dir/specs"
interest_specs_file="$specs_output_folder/interest-specs.csv"

log_file="$output_dir/${class_name}_${method}-second-round-validation.log"

# Clear log file
echo "" >"$log_file"

# Prepare files
mkdir -p "$daikon_output_folder"
mkdir -p "$specs_output_folder"

# Find the build file
build_file_dir=""
current_dir="$target_class"
while [ "$current_dir" != "/" ]; do
    build_file_dir=$(find "$current_dir" -maxdepth 1 -name "build.gradle" -o -name "pom.xml" | head -n 1)
    if [ -n "$build_file_dir" ]; then
        break
    fi
    current_dir=$(dirname "$current_dir")
done
if [ -z "$build_file_dir" ]; then
    echo "Build file not found"
    exit 1
fi

# Subject classpath
subject_sources=$(dirname "$build_file_dir")
subject_cp="$subject_sources/build/libs/*"
# Prepare classpath for Daikon
cp_for_daikon="libs/*:$subject_cp"

# Run script
echo "### Running second round validation for $target_class" | tee -a "$log_file"
echo "# Class: $class_name" | tee -a "$log_file"
echo "# Method: $method" | tee -a "$log_file"
echo "# Invariants file: $specfuzzer_invs_file" | tee -a "$log_file"
echo "# Assertions file: $specfuzzer_assertions_file" | tee -a "$log_file"

if [[ ! -f "$target_class" ]]; then
    echo "Error: Class file $target_class not found!"
    exit 1
fi
if [[ ! -f "$specfuzzer_invs_file" ]]; then
    echo "Error: Invariants file $specfuzzer_invs_file not found!"
    exit 1
fi
if [[ ! -f "$specfuzzer_assertions_file" ]]; then
    echo "Error: Assertions file $specfuzzer_assertions_file not found!"
    exit 1
fi

# Recompile the subject
echo "> Recompiling subject: $target_class" | tee -a "$log_file"
python3 scripts/compile_subject.py "$subject_sources"

# Perform the Dynamic Comparability Analysis
echo '> Performing Dynamic Comparability Analysis from driver: '"$test_suite_driver" | tee -a "$log_file"
java -cp "$cp_for_daikon" daikon.DynComp "$driver_fqname" --output-dir="$daikon_output_folder"

# Run Chicory on the existing testsuite to create the valid trace
echo '> Running Chicory for dtrace generation from driver: '"$test_suite_driver" | tee -a "$log_file"
objects_file="$daikon_output_folder/${test_suite_driver}-objects.xml"
cmp_file="$daikon_output_folder/${test_suite_driver}.decls-DynComp"
java -cp "$cp_for_daikon" daikon.Chicory \
    --output-dir="$daikon_output_folder" \
    --comparability-file="$cmp_file" \
    --ppt-omit-pattern="${test_suite_driver}.*" \
    "$driver_fqname" \
    "$objects_file" >>"$log_file" 2>&1

# Run Daikon Invariant Checker to validate the invariants
echo '> Running Daikon Invariant Checker from driver: '"$test_suite_driver" | tee -a "$log_file"
dtrace_file="$daikon_output_folder/${test_suite_driver}.dtrace.gz"
java -Xmx8g -cp "$cp_for_daikon" daikon.tools.InvariantChecker \
    --conf \
    --serialiazed-objects "$objects_file" \
    "$specfuzzer_invs_file" \
    "$dtrace_file" \
    >/dev/null

mv invs.csv "$daikon_output_folder"
rm invs_file.xml

# Save the specfications of interest, i.e., the postconditions or object invariants
echo "> Saving invariants of interest" | tee -a "$log_file"
python3 scripts/filter_invariants_of_interest.py "$daikon_output_folder/invs.csv" "$target_class_fqname" "$method" >>"$log_file" 2>&1

# Extract the assertions that are not discarded by the invariant checker
echo "> Extracting non-filtered assertions" | tee -a "$log_file"
python3 scripts/extract_non_filtered_assertions.py "$specfuzzer_assertions_file" "$interest_specs_file" "$class_name" "$method" >>"$log_file" 2>&1

echo "> Done" | tee -a "$log_file"
echo "Output is saved in ${output_dir}"
