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
tests_dir="$subject_output_dir/tests"
specs_per_test_dir="$tests_dir/specs_per_test"
log_file="$subject_output_dir/${class_name}_${method}-test-by-test-analysis.log"

# Create directories if they don't exist
mkdir -p "$specs_per_test_dir"

echo "==> Running test-by-test specification filtering analysis for $target_class" | tee -a "$log_file"
echo "Class: $class_name" | tee -a "$log_file"
echo "Method: $method" | tee -a "$log_file"
echo "Invariants file: $invs_file" | tee -a "$log_file"
echo "Assertions file: $assertions_file" | tee -a "$log_file"
echo "Tests directory: $tests_dir" | tee -a "$log_file"

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

# Base name for test class and driver
test_class_name="${class_name}Tester"

# Recompile the subject
echo "> Recompiling subject: $target_class" | tee -a "$log_file"
python3 scripts/compile_subject.py "$subject_sources"

# Find all compilable test files
test_files=$(find "$tests_dir" -name "test*llm.java" -o -name "test*evosuite.java" | sort)

echo "> Found $(echo "$test_files" | wc -l) compilable test files" | tee -a "$log_file"

# Process each test file individually
for test_file in $test_files; do
    test_name=$(basename "$test_file" .java)
    echo "Processing test: $test_name" | tee -a "$log_file"

    # Create temporary directory for this test's analysis
    temp_dir="$specs_per_test_dir/temp_$test_name"
    mkdir -p "$temp_dir"

    # Create a temporary driver file with only this test
    driver_file="$temp_dir/${test_class_name}SingleTestDriver.java"

    # Create the driver file
    echo "package testers;" >"$driver_file"
    echo "" >>"$driver_file"
    echo "import org.junit.runner.JUnitCore;" >>"$driver_file"
    echo "import org.junit.runner.Result;" >>"$driver_file"
    echo "import org.junit.runner.notification.Failure;" >>"$driver_file"
    echo "" >>"$driver_file"
    echo "public class ${test_class_name}SingleTestDriver {" >>"$driver_file"
    echo "    public static void main(String[] args) {" >>"$driver_file"
    echo "        Result result = JUnitCore.runClasses(SingleTest.class);" >>"$driver_file"
    echo "        for (Failure failure : result.getFailures()) {" >>"$driver_file"
    echo "            System.out.println(failure.toString());" >>"$driver_file"
    echo "        }" >>"$driver_file"
    echo "        System.out.println(\"Tests run: \" + result.getRunCount() + \", Failures: \" + result.getFailureCount());" >>"$driver_file"
    echo "    }" >>"$driver_file"
    echo "}" >>"$driver_file"

    # Create the single test class file
    single_test_file="$temp_dir/SingleTest.java"

    # Extract the test method from the original file
    test_method=$(grep -A 50 "@Test" "$test_file" | sed -n '/public void test/,/^    }/p')

    # Create a new test class with just the single test
    echo "import org.junit.Test;" >"$single_test_file"
    echo "import static org.junit.Assert.*;" >>"$single_test_file"
    echo "" >>"$single_test_file"
    echo "public class SingleTest {" >>"$single_test_file"
    echo "$test_method" >>"$single_test_file"
    echo "}" >>"$single_test_file"

    # Compile the test and driver
    echo "> Compiling single test and driver for $test_name" | tee -a "$log_file"
    javac -cp "$cp_for_daikon:$JUNIT_JAR" "$single_test_file" "$driver_file"

    # If compilation succeeded, run the dynamic analysis
    if [ $? -eq 0 ]; then
        echo "> Running dynamic analysis for $test_name" | tee -a "$log_file"

        # Create output folders for this test
        daikon_output_folder="$temp_dir/daikon"
        specs_output_folder="$temp_dir/specs"
        mkdir -p "$daikon_output_folder"
        mkdir -p "$specs_output_folder"

        # Run driver name
        driver_name="${test_class_name}SingleTestDriver"
        driver_fqname="testers.${driver_name}"

        # Perform Dynamic Comparability Analysis
        echo '> Performing Dynamic Comparability Analysis for '"$test_name" | tee -a "$log_file"
        java -cp "$cp_for_daikon:$temp_dir" daikon.DynComp "$driver_fqname" --output-dir="$daikon_output_folder"

        # Run Chicory on the single test to create the trace
        echo '> Running Chicory for dtrace generation for '"$test_name" | tee -a "$log_file"
        objects_file="$daikon_output_folder/${driver_name}-objects.xml"
        cmp_file="$daikon_output_folder/${driver_name}.decls-DynComp"
        java -cp "$cp_for_daikon:$temp_dir" daikon.Chicory \
            --output-dir="$daikon_output_folder" \
            --comparability-file="$cmp_file" \
            --ppt-omit-pattern="${driver_name}.*" \
            "$driver_fqname" \
            "$objects_file" >>"$log_file" 2>&1

        # Run Daikon Invariant Checker to validate the invariants with this test
        echo '> Running Daikon Invariant Checker for '"$test_name" | tee -a "$log_file"
        dtrace_file="$daikon_output_folder/${driver_name}.dtrace.gz"
        java -Xmx8g -cp "$cp_for_daikon:$temp_dir" daikon.tools.InvariantChecker \
            --conf \
            --serialiazed-objects "$objects_file" \
            "$invs_file" \
            "$dtrace_file" \
            >/dev/null

        # Move and save invariants CSV
        mv invs.csv "$daikon_output_folder"
        rm -f invs_file.xml

        # Save the specifications of interest
        interest_specs_file="$specs_output_folder/interest-specs.csv"
        echo "> Saving invariants of interest for $test_name" | tee -a "$log_file"
        python3 scripts/filter_invariants_of_interest.py "$daikon_output_folder/invs.csv" "$target_class_fqname" "$method" >>"$log_file" 2>&1

        # Extract the assertions that are not discarded by the invariant checker
        output_assertions_file="$specs_per_test_dir/${test_name}.txt"
        echo "> Extracting filtered assertions for $test_name" | tee -a "$log_file"
        python3 scripts/extract_non_filtered_assertions.py "$assertions_file" "$interest_specs_file" "$class_name" "$method" >"$output_assertions_file" 2>>"$log_file"

        # Count the filtered specs and add summary to the output file
        filtered_count=$(grep -c "^" "$output_assertions_file" || echo "0")
        echo -e "\n=== Summary ===" >>"$output_assertions_file"
        echo "Test: $test_name" >>"$output_assertions_file"
        echo "Filtered specifications: $filtered_count" >>"$output_assertions_file"

        echo "> Test $test_name filtered $filtered_count specifications" | tee -a "$log_file"
    else
        echo "! Failed to compile test and driver for $test_name" | tee -a "$log_file"
    fi

    # Optional: cleanup temp files to save space
    # rm -rf "$temp_dir"
done

echo "> Completed test-by-test specification analysis" | tee -a "$log_file"
echo "Results are saved in $specs_per_test_dir"
