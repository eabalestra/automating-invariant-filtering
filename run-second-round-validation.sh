#!/bin/bash
source scripts/init_env.sh
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
invs_file="$SPECS_DIR/$subject_name/output/$class_name-$method-specfuzzer-1.inv.gz"
assertions_file="$SPECS_DIR/$subject_name/output/$class_name-$method-specfuzzer-1.assertions"

test_class_name="${class_name}Tester"
driver_name="${test_class_name}Driver"
test_suite_driver="${driver_name}Augmented"
driver_fqname="testers.${test_suite_driver}"

# Output files
OUTPUT_FOLDER="output"
subject_dir="$OUTPUT_FOLDER/${class_name}_${method}"
daikon_output_folder="$subject_dir/daikon"
specs_output_folder="$subject_dir/specs"
interest_specs_file="$specs_output_folder/interest-specs.csv"

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
echo "==> Running second round validation for $target_class"
echo "- Class: $class_name"
echo "- Method: $method"
echo "- Invariants file: $invs_file"
echo "- Assertions file: $assertions_file"

# Recompile the subject
echo "> Recompiling subject: $target_class"
current_dir=$(pwd)
cd "$subject_sources" || exit
./gradlew -q -Dskip.tests jar
cd "$current_dir" || exit

# Perform the Dynamic Comparability Analysis
echo '> Performing Dynamic Comparability Analysis from driver: '"$test_suite_driver"
java -cp "$cp_for_daikon" daikon.DynComp "$driver_fqname" --output-dir="$daikon_output_folder"

# Run Chicory on the existing testsuite to create the valid trace
echo '> Running Chicory for dtrace generation from driver: '"$test_suite_driver"
objects_file="$daikon_output_folder/${test_suite_driver}-objects.xml"
cmp_file="$daikon_output_folder/${test_suite_driver}.decls-DynComp"
java -cp "$cp_for_daikon" daikon.Chicory \
    --output-dir="$daikon_output_folder" \
    --comparability-file="$cmp_file" \
    --ppt-omit-pattern="${test_suite_driver}.*" \
    "$driver_fqname" \
    "$objects_file"

# Run Daikon Invariant Checker to validate the invariants
echo '> Running Daikon Invariant Checker from driver: '"$test_suite_driver"
dtrace_file="$daikon_output_folder/${test_suite_driver}.dtrace.gz"
java -Xmx8g -cp "$cp_for_daikon" daikon.tools.InvariantChecker \
    --conf \
    --serialiazed-objects "$objects_file" \
    "$invs_file" \
    "$dtrace_file" \
    >/dev/null

mv invs.csv "$daikon_output_folder"
rm invs_file.xml

# Save the specfications of interest, i.e., the postconditions or object invariants
echo "> Saving invariants of interest"
python3 scripts/filter_invariants_of_interest.py "$daikon_output_folder/invs.csv" "$target_class_fqname" "$method"

# Extract the assertions that are not discarded by the invariant checker
echo "> Extracting non-filtered assertions"
python3 scripts/extract_non_filtered_assertions.py "$assertions_file" "$interest_specs_file" "$class_name" "$method"

echo "> Done"
echo "Output is saved in ${subject_dir}"
