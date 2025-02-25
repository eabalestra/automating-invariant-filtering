#!/bin/bash

[ -z "$SUBJECTS_DIR" ] && {
    echo "> The environment variable SUBJECTS_DIR is not set"
    exit 1
}
[ -z "$SPECS_DIR" ] && {
    echo "> The environment variable SPECS_DIR is not set"
    exit 1
}
[ -z "$DAIKONDIR" ] && {
    echo "> The environment variable DAIKONDIR is not set"
    exit 1
}
[ -z "$VIRTUAL_ENV" ] && {
    echo "> The virtual environment is not activated"
    exit 1
}

subject_name=$2
target_class_fqname=$3
method_name=$4

LIGHT_BLUE="\033[94m"
BOLD="\033[1m"
RESET="\033[0m"

echo "${LIGHT_BLUE}${BOLD}Running automatic invariant filtering for $target_class_fqname::$method_name${RESET}"

if [ "$1" = "--llm-test-aug" ]; then
    class_name="${target_class_fqname##*.}"
    test_suite=$5
    test_driver=$6
    ./run-automatic-invariant-filtering.sh "$subject_name" "$class_name" "$method_name" "$test_suite" "$test_driver"
    exit 0
fi

if [ "$1" = "--daikon-val-filter" ]; then
    ./run-second-round-validation.sh "$subject_name" "$target_class_fqname" "$method_name"
    exit 0
fi

echo './tool.sh: invalid option: '"$1"
echo 'usage: ./tool.sh --llm-test-aug <subject_name> <target_class> <method> <test_suite> <test_driver>'
echo '       ./tool.sh --daikon-val-filter <subject_name> <target_class> <method>'
exit 1
