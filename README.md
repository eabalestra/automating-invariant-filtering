# automating-invariant-filtering

## Requirements
- Python 3.6 or higher
- [Ollama](https://ollama.com/)

## Installation and Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama create test-generation-model -f testgen/Modelfile
ollama run test-generation-model (the model will keep running)
```

## Usage
```bash
sh run-automatic-invariant-filtering.sh <class_file>.java <specs_file> <method_under_test> <test_suite_file>.java <test_driver_file>.java
```

### Example
```bash
sh run-automatic-invariant-filtering.sh examples/simple-examples_getMin/src/main/java/examples/SimpleMethods.java examples/simple-examples_getMin/specs/SimpleMethods-getMin-specfuzzer-1.assertions getMin examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTester0.java examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTesterDriver.java
```