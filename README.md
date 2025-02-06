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
python search-counterexample.py <class_file>.java <specs_file>.csv <method_under_test>  
```
### Example
```bash
python search-counterexample.py examples/ArithmeticUtils/Multiplier.java examples/ArithmeticUtils/multiply_specs.csv multiply
```