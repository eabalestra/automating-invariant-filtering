#!/bin/bash
# Script to analyze which specifications are filtered by each individual test

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
assertions_file="$SPECS_DIR/$subject_name/output/$class_name-$method-specfuzzer-1-buckets.assertions"

# Output structure
OUTPUT_FOLDER="output"
subject_output_dir="$OUTPUT_FOLDER/${class_name}_${method}"
tests_dir="$subject_output_dir/test"
specs_per_test_dir="$tests_dir/specs_per_test"
log_file="$subject_output_dir/${class_name}_${method}-test-by-test-analysis.log"

# Create directories if they don't exist
mkdir -p "$specs_per_test_dir"

echo "### Test-by-test spec filtering analysis: $class_name.$method" | tee -a "$log_file"
echo "# Class: $class_name" | tee -a "$log_file"
echo "# Method: $method" | tee -a "$log_file"
echo "# Invariants file: $invs_file" | tee -a "$log_file"
echo "# Assertions file: $assertions_file" | tee -a "$log_file"

if [[ ! -f "$target_class" ]]; then
    echo "Error: Class file $target_class not found!"
    exit 1
fi
if [[ ! -f "$invs_file" ]]; then
    echo "Error: Invariants file $invs_file not found!"
    exit 1
fi
if [[ ! -f "$assertions_file" ]]; then
    echo "Error: Assertions file $assertions_file not found!"
    exit 1
fi

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

# Find compilable test files
llm_compilable_test_file=$(find "$tests_dir" -name "*LlmCompilableTest.java" | sort)

# Check if the test file exists
test_files_path="$tests_dir/tests"
if [ -d "$test_files_path" ]; then
    rm -rf "$test_files_path"
fi
mkdir -p "$test_files_path"

# Split the test suite into individual test files
python3 scripts/test_splitter.py "$llm_compilable_test_file" "$test_files_path"

# Run Daikon on the test files
for test_file in "$test_files_path"/*; do
    echo "> Processing test file: $test_file" | tee -a "$log_file"
    test_name=$(basename "$test_file" .txt)

    # Create the test file
    tester_file_name="${test_files_path}/${test_name}Tester.java"

    {
        echo "package testers;"
        echo ""
        echo "import org.junit.FixMethodOrder;"
        echo "import org.junit.Test;"
        echo "import org.junit.runners.MethodSorters;"
        echo ""
        echo "@FixMethodOrder(MethodSorters.NAME_ASCENDING)"
        echo "public class ${test_name}Tester {"
        echo ""
        echo "    public static boolean debug = false;"
        echo ""
        cat "$test_file"
        echo ""
        echo "}"
    } >>"$tester_file_name"

    # Create the driver file
    driver_file_name="${test_files_path}/${test_name}TesterDriver.java"
    {
        echo "package testers;"
        echo ""
        echo "public class ${test_name}TesterDriver {"
        echo ""
        echo "    public static void main(String... args) {"
        echo "        boolean hadFailure = false;"
        echo "        ${test_name}Tester t0 = new ${test_name}Tester();"
        echo "        try {"
        echo "            t0.${test_name}();"
        echo "        } catch (Throwable e) {"
        echo "            hadFailure = true;"
        echo "            e.printStackTrace();"
        echo "        }"
        echo "        if (hadFailure) {"
        echo "            System.exit(1);"
        echo "        }"
        echo "    }"
        echo "}"
    } >>"$driver_file_name"

    # Compile the test file
    echo "Compiling test file: $tester_file_name" | tee -a "$log_file"
    javac -cp "$cp_for_daikon" "$tester_file_name" "$driver_file_name" -d "$tests_dir"
    if [ $? -ne 0 ]; then
        echo "Error: Compilation failed for $tester_file_name" | tee -a "$log_file"
        continue
    fi

    # Perform the Dynamic Comparability Analysis
    echo "Performing Dynamic Comparability Analysis from driver: $driver_file_name" | tee -a "$log_file"
    java -cp "$cp_for_daikon":"$tests_dir" daikon.DynComp "testers.${test_name}TesterDriver" --output-dir="$specs_per_test_dir"
    if [ $? -ne 0 ]; then
        echo "Error: Daikon analysis failed for $test_file" | tee -a "$log_file"
        continue
    fi

    # Run Chicory on the existing testsuite to create the valid trace
    echo "Running Chicory on the existing testsuite to create the valid trace" | tee -a "$log_file"

    echo ''
done

echo "> Completed test-by-test specification analysis" | tee -a "$log_file"
echo "Results are saved in $specs_per_test_dir"
