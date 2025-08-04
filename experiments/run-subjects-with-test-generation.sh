#!/bin/bash

# Default values
DEFAULT_MODELS="L_Llama318Instruct"
DEFAULT_PROMPTS="General_V1"

# Initialize variables
MODELS="$DEFAULT_MODELS"
PROMPTS="$DEFAULT_PROMPTS"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
    -m | --models)
        MODELS="$2"
        shift 2
        ;;
    -p | --prompts)
        PROMPTS="$2"
        shift 2
        ;;
    -h | --help)
        echo "Usage: $0 [OPTIONS]"
        echo "  -m, --models MODELS     Models to use (default: $DEFAULT_MODELS)"
        echo "  -p, --prompts PROMPTS   Prompts to use (default: $DEFAULT_PROMPTS)"
        echo "  -h, --help              Show this help"
        exit 0
        ;;
    *)
        echo "Error: Unknown option $1"
        exit 1
        ;;
    esac
done

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
    set -- $subject

    echo "Running tool with arguments: $1, $2, $3"
    echo "Progress: $percentage% ($current_line/$total_lines)"

    ./run-automatic-invariant-filtering.sh "$1" "$2" "$3" -m $MODELS -p $PROMPTS

    if [[ $? -ne 0 ]]; then
        echo "Error: Tool execution failed for subject $subject"
        exit 1
    fi

done <"$SUBJECTS_FILE"
