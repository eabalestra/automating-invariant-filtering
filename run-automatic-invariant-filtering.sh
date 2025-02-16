#!/bin/bash

# parameters
SUBJECT_CLASS_PATH=$1
SPECS_FILE_PATH=$2
METHOD_NAME=$3
EXISTING_TEST_FILE_PATH=$4
EXISTING_TEST_DRIVER_PATH=$5

# copy the existing test suite
cp "$EXISTING_TEST_FILE_PATH" "${EXISTING_TEST_FILE_PATH%.java}Augmented.java"
COPY_EXISTING_TEST_FILE_PATH="${EXISTING_TEST_FILE_PATH%.java}Augmented.java"
cp "$EXISTING_TEST_DRIVER_PATH" "${EXISTING_TEST_DRIVER_PATH%.java}Augmented.java"
COPY_EXISTING_TEST_DRIVER_PATH="${EXISTING_TEST_DRIVER_PATH%.java}Augmented.java"

# call the search-counterexample.py script, which will generate the tests and save them in the output folder
echo "> Generate tests using LLM"
python search-counterexample.py "$SUBJECT_CLASS_PATH" "$SPECS_FILE_PATH" "$METHOD_NAME"

# append the generated tests by LLM to the existing test suite
GENERATED_TEST_FILE="output/test/$(basename "$SUBJECT_CLASS_PATH" .java)/$(basename "$SUBJECT_CLASS_PATH" .java)_${METHOD_NAME}LlmTest.java"
echo "> Append the generated tests to the existing test suite"
python scripts/test_appender.py "$COPY_EXISTING_TEST_FILE_PATH" "$COPY_EXISTING_TEST_DRIVER_PATH" "$GENERATED_TEST_FILE" "$SUBJECT_CLASS_PATH"