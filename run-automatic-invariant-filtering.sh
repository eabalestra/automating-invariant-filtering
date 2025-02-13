#!/bin/bash

# parameters
CLS=$1
CSV_FILE=$2
METHOD_NAME=$3
EXISTING_TEST_FILE=$4

# copy the existing test suite
cp "$EXISTING_TEST_FILE" "${EXISTING_TEST_FILE%.java}Augmented.java"
COPY_EXISTING_TEST_FILE="${EXISTING_TEST_FILE%.java}Augmented.java"

# call the search-counterexample.py script, which will generate the tests and save them in the output folder
echo "> Running search-counterexample.py"
python search-counterexample.py "$CLS" "$CSV_FILE" "$METHOD_NAME"

# append the generated tests by llm to the existing test suite
GENERATED_TEST_FILE="output/test/$(basename "$CLS" .java)/$(basename "$CLS" .java)_${METHOD_NAME}-llm-tests.java"
echo "> Append the generated tests to the existing test suite"
python scripts/append_test_suites.py "$COPY_EXISTING_TEST_FILE" "$GENERATED_TEST_FILE"