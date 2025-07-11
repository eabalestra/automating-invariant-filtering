# Run Experiments with Specfuzzer Subjects

## Run Subjects with Test Generation

This script automates the execution of the automatic invariant filtering process for multiple test subjects using Large Language Models (LLMs) for test generation.

### Usage

#### Basic Syntax

```bash
./run-subjects-with-test-generation.sh [OPTIONS]
```

#### Available Options

| Option            | Description                           | Default Value        |
| ----------------- | ------------------------------------- | -------------------- |
| `-m`, `--models`  | Specifies the LLM models to use       | `L_Llama318Instruct` |
| `-p`, `--prompts` | Specifies the prompt templates to use | `General_V1`         |
| `-h`, `--help`    | Shows command help                    | -                    |
