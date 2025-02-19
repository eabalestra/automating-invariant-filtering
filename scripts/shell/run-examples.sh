#!/bin/bash
echo "==> Running examples"

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not activated. Exiting."
    exit 1
fi

run_example() {
    local method_name="$1"
    local subject="$2"
    local src_file="$3"
    local test_file="$4"
    local test_driver="$5"
    local output_dir="$6"

    local i=1
    echo "==> Running example N°$i for $subject"
    mkdir -p "$output_dir"
    for specs in "examples/${subject}/specs/"*; do
        echo "==> Running example for spec: $specs"
        sh run-automatic-invariant-filtering.sh "$src_file" "$specs" "$method_name" "$test_file" "$test_driver"
        local test_augmented_file="${test_file%.*}Augmented.java"
        local test_driver_augmented_file="${test_driver%.*}Augmented.java"
        if [ -f "$test_augmented_file" ]; then
            mv "$test_augmented_file" "$output_dir/$(basename "${test_augmented_file%.*}")-$i.${test_augmented_file##*.}"
            mv "$test_driver_augmented_file" "$output_dir/$(basename "${test_driver_augmented_file%.*}")-$i.${test_driver_augmented_file##*.}"
            i=$((i + 1))
        else
            echo "File $test_augmented_file does not exist. Skipping."
        fi
    done
}

run_example "clamp" "MathUtil_clamp" \
    "examples/MathUtil_clamp/src/main/java/jts/MathUtil.java" \
    "examples/MathUtil_clamp/src/test/java/testers/MathUtilTester0.java" \
    "examples/MathUtil_clamp/src/test/java/testers/MathUtilTesterDriver.java" \
    "output/test/MathUtil"

# run_example "getMin" "simple-examples_getMin" \
#    "examples/simple-examples_getMin/src/main/java/examples/SimpleMethods.java" \
#    "examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTester0.java" \
#    "examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTesterDriver.java" \
#    "output/test/SimpleMethods"
