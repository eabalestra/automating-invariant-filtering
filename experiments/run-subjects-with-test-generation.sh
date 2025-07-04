#!/bin/bash

# Path to the file containing the list of subjects
SUBJECTS_FILE="experiments/subjects-to-run"

# Check if the file exists
if [[ ! -f "$SUBJECTS_FILE" ]]; then
    echo "Error: $SUBJECTS_FILE not found!"
    exit 1
fi

# Count the total number of lines (excluding empty lines and comments)
total_lines=$(grep -v -e '^#' -e '^$' "$SUBJECTS_FILE" | wc -l)
current_line=0

# Loop through each subject in the file and execute the tool
while IFS= read -r subject; do
    # Skip empty lines or lines starting with '#'
    [[ -z "$subject" || "$subject" =~ ^# ]] && continue

    # Increment the current line counter
    ((current_line++))

    # Calculate the percentage of completion
    percentage=$((current_line * 100 / total_lines))

    # Clear positional parameters and split the subject line into arguments
    set -- "$subject"

    class_name="${2##*.}"
    test_suite=$class_name"Tester0"
    test_driver=$class_name"TesterDriver"

    echo "Running tool with arguments: $1, $2, $3, $test_suite, $test_driver"
    echo "Progress: $percentage% ($current_line/$total_lines)"

    ./run-automatic-invariant-filtering.sh "$1" "$2" "$3" -models "L_Llama318Instruct" -p "General_V1" >/dev/null 2>&1

    if [[ $? -ne 0 ]]; then
        echo "Error: Tool execution failed for subject $subject"
        exit 1
    fi

done <"$SUBJECTS_FILE"
