#!/bin/bash

[ -z "$DAIKONDIR" ] && {
    echo "> The environment variable DAIKONDIR is not set"
    exit 1
}

# Arguments
subject="$1"
fqname="$2"
method_name="$3"
invs_file="$4"
dot_assertions_file="$5"

class_name="${fqname##*.}"
test_class_name="${class_name}Tester"
driver_name="${test_class_name}Driver"
augmented_driver="${driver_name}Augmented"
driver_fqname="testers.${augmented_driver}"

# Directories
# navigate to the directory containing the build file
build_file_dir=""
current_dir="$subject"
while [ "$current_dir" != "/" ]; do
    build_file_dir=$(find "$current_dir" -maxdepth 1 -name "build.gradle" -o -name "pom.xml" | head -n 1)
    if [ -n "$build_file_dir" ]; then
        break
    fi
    current_dir=$(dirname "$current_dir")
done

subject_sources=$(dirname "$build_file_dir")
automating_if_subject_dir="output/${class_name}_${method_name}"

echo "Subject: $subject"
echo "Subject dir: $subject_sources"
echo "> Recompiling subject: $subject"
current_dir=$(pwd)
cd "$subject_sources" || exit
./gradlew -q -Dskip.tests jar
cd "$current_dir" || exit

subject_cp="$subject_sources/build/libs/*"
cp_for_daikon="libs/*:$subject_cp"

daikon_output_dir="$automating_if_subject_dir/daikon"
mkdir -p "$daikon_output_dir"

echo "> Running DynComp from driver: ${driver_fqname}"
java -cp "$cp_for_daikon" daikon.DynComp "$driver_fqname" --output-dir="$daikon_output_dir"

echo '> Running Chicory for dtrace generation from driver: '"${driver_fqname}"
java -cp "$cp_for_daikon" daikon.Chicory \
    --output-dir="$daikon_output_dir" \
    --comparability-file="$daikon_output_dir/${augmented_driver}.decls-DynComp" \
    --ppt-omit-pattern="${augmented_driver}.*" \
    "$driver_fqname" \
    "$daikon_output_dir/${augmented_driver}-objects.xml"

echo "> Running Daikon Invariant Checker"
java -Xmx8g -cp "$cp_for_daikon" daikon.tools.InvariantChecker \
    --conf \
    --serialiazed-objects "$daikon_output_dir/${augmented_driver}-objects.xml" \
    "$invs_file" \
    "$daikon_output_dir/${augmented_driver}.dtrace.gz"

mkdir -p "$automating_if_subject_dir/specs"

echo "> Filtering invariants"
python3 scripts/filter_invariants_of_interest.py invs.csv "$fqname" "$method_name"
filtered_invs_file="$automating_if_subject_dir/specs/filtered-specs.csv"

echo "> Extracting non-filtered assertions"
python3 scripts/extract_non_filtered_assertions.py "$dot_assertions_file" "$filtered_invs_file" "$class_name" "$method_name"
