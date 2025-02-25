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

subject_name=$2
target_class_fqname=$3
method_name=$4

LIGHT_BLUE="\033[94m"
WHITE="\033[97m"
YELLOW="\033[93m"
RESET="\033[0m"

echo "${LIGHT_BLUE}╔════════════════════════╗${RESET}"
echo "${WHITE}║      ${YELLOW}${BOLD}AUTOMATIC-IF ${RESET}${WHITE}     ║${RESET}"
echo "${LIGHT_BLUE}╚════════════════════════╝${RESET}"

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
echo 'usage: ./tool.sh --gen-llm-suite <subject_name> <target_class> <method> <test_suite> <test_driver>'
echo '       ./tool.sh --second-round-validation <subject_name> <target_class> <method>'
exit 1
