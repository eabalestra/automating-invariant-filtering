# automating-invariant-filtering

## Requirements
- Python 3.6 or higher
- [Ollama](https://ollama.com/)

## Installation and Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama create test-generation-model -f test-generation/Modelfile
ollama run test-generation-model (the model will keep running)
```

## Usage
```bash
python main.py <java_file> <specs_file>.csv <method_under_test>>  
```
### Example
```bash
python main.py Stack.java stakc_specs.csv push
```