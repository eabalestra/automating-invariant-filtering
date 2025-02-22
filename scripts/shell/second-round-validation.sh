#!/bin/bash
# You need to be in a Docker container with the specfuzzer tool and in the /specfuzzer directory

echo "Running second round validation"
if [ "$#" -ne 5 ]; then
    echo "Illegal number of parameters."
    echo "Usage: $0 <gassert_subject> <fully.qualified.ClassName> <method_name> <invs_file>.inv.gz <assertions>.assertions"
    exit 1
fi

# Arguments
gassert_subject="$1"
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
lib_dir="lib"
gassert_dir="../tools/GAssert"
subject_sources="${gassert_dir}/subjects/${gassert_subject}"
automating_if_subject_dir="automating-invariant-filtering/output/${class_name}_${method_name}"

# create output directory
mkdir -p "$automating_if_subject_dir/specs"

echo "Subject: $gassert_subject"
echo "GAssert dir: $gassert_dir"
echo "> Recompiling GAssert subject: $gassert_subject"
current_dir=$(pwd)
cd "$subject_sources" || exit
./gradlew -q -Dskip.tests jar
cd "$current_dir" || exit

# Locate the built jar file
subject_jar=$(find "${subject_sources}/build/libs" -name "*.jar" | head -n 1)
if [ -z "$subject_jar" ]; then
    echo "Error: subject jar not found in ${subject_sources}/build/libs"
    exit 1
fi
echo "> Using subject jar: $subject_jar"

echo "> Running daikon.DynComp with driver: $driver_fqname"
output_dir="example-trace-generation"
mkdir -p "$output_dir"
java -cp "${lib_dir}/daikon.jar:${subject_jar}" daikon.DynComp "$driver_fqname" --output-dir="$output_dir"

echo "> Running daikon.Chicory with driver: $driver_fqname"
java -cp "${lib_dir}/daikon.jar:${subject_jar}" daikon.Chicory \
    --output-dir="$output_dir" \
    --comparability-file="$output_dir/${augmented_driver}.decls-DynComp" \
    --ppt-omit-pattern="${augmented_driver}.*" \
    "$driver_fqname" \
    "$output_dir/${augmented_driver}-objects.xml"

echo "> Running daikon.tools.InvariantChecker"
java -Xmx8g -cp "lib/*:${subject_jar}" daikon.tools.InvariantChecker \
    --conf \
    --serialiazed-objects "$output_dir/${augmented_driver}-objects.xml" \
    "$invs_file" \
    "$output_dir/${augmented_driver}.dtrace.gz" \
    >>"$output_dir/${class_name}_${method_name}.log"

echo "> Filtering invariants"
python3 automating-invariant-filtering/scripts/filter_invariants_of_interest.py invs.csv "$fqname" "$method_name"
filtered_invs_file="$automating_if_subject_dir/specs/filtered-specs.csv"

echo "> Extracting non-filtered assertions"
python3 automating-invariant-filtering/scripts/extract_non_filtered_assertions.py "$dot_assertions_file" "$filtered_invs_file" "$class_name" "$method_name"
