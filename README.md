# Automating Invariant Filtering

## 📑 Table of Contents

- [Prerequisites](#prerequisites)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Output Structure](#output-structure)
- [Experiments](#experiments)

## Prerequisites

This tool is designed to complement the SpecFuzzer tool. Therefore, it requires as input the various files produced by SpecFuzzer (`<subject>-1-buckets.assertion`, `<subject>-1.assertions`, `<subject>-1.inv.gz`, `<subject>-invs-by-mutants.csv`).

For more information, visit [SpecFuzzer repository](https://github.com/facumolina/specfuzzer).

## Requirements

- Java 8
- Python 3.6 or higher
- [Ollama](https://ollama.com/) for running LLMs locally

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/eabalestra/automating-invariant-filtering.git
cd automating-invariant-filtering
```

### 2. Install Daikon

- Download the required Daikon version from [this link](https://mega.nz/file/pPgmnCST#dObECd8W5VeIDz5xzSgeQnhmH_-BRnOzt1VKaGn7Ihg).  
  Or use mega-tools:

```bash
# (Use mega-tools if preferred)
```

- Unzip the archive:

```bash
unzip /path/to/daikon-5.8.2.zip -d /desired/location
```

- Set the following in `config/setup_env.sh`:

```bash
DAIKONDIR=/desired/location/daikon-5.8.2
```

### 3. Install Ollama and Pull Models

- Install Ollama following its documentation.
- Pull the LLM models you intend to use, for example:

```bash
ollama pull llama-3b-instruct
```

### 4. Configure Environment Variables

Set variables manually by running:

```bash
source config/setup_env.sh
```

If you plan to use models from OpenAI, Google, or Hugging Face, you will also need to set their respective API keys:

```bash
# Environment variables for directories
export DAIKONDIR=/desired/location/daikon-5.8.2
export SPECS_DIR=/path/to/your/specfuzzer-outputs
export SUBJECTS_DIR=/path/to/your/subjects

# Environment variables for API keys
export OPENAI_API_KEY=
export GOOGLE_API_KEY=
export API_KEY_HUGGINGFACE=
```

### 5. Create and Activate Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r config/requirements.txt
```

## Usage

The tool provides several scripts for different stages:

1. **Automatic Invariant Filtering**: For each specification (postcondition) of the subject found in the `<subject>-1-buckets.assertions` file produced by SpecFuzzer, the tool attempts to generate a test that invalidates the postcondition using an LLM. Additionally, each compilable test is added to the original test suite of the subject.

2. **Second Round Validation**: Once the new test suite is generated with the new tests, specifications invalidated by the new test suite are discarded.

## Example

```bash
# Step 1: Run automatic filtering with LLM test generation
./run-automatic-invariant-filtering.sh QueueAr_getFront DataStructures.QueueAr getFront -models "llama-3b-instruct" -p "General_V1"

# Step 2: Validate with enhanced test suite
./run-second-round-validation.sh QueueAr_getFront DataStructures.QueueAr getFront
```

## Output Structure

```
output/
└─ QueueAr_getFront/
   ├─ QueueAr_getFront.log
   ├─ QueueAr_getFront-second-round-validation.log
   ├─ test/              # Generated LLM tests
   ├─ specs/             # Filtered and surviving specs
   └─ daikon/            # Daikon analysis outputs
```

## Experiments

To simulate the experiments used in the research work, in addition to the installation steps mentioned above, you must:

1. Clone the following repository containing the outputs of the subjects used as experiments in SpecFuzzer:

```bash
git clone https://github.com/eabalestra/specfuzzer-subject-results.git
```

Set the environment variable in `config/setup_env.sh`:

```bash
export SPECS_DIR=specfuzzer-subject-results/specfuzzer-outputs
```

2. Download the subjects used in SpecFuzzer (GAssert subjects) from [this link](https://drive.google.com/file/d/1wMb6KE0rN3r83RC-NsP3xG6zwYduw57i/view?usp=sharing).

```bash
unzip /path/to/GAssert.zip -d /desired/location
```

Set the environment variable in `config/setup_env.sh`:

```bash
export SUBJECTS_DIR=/desired/location/GAssert/subjects
```

3. If you want to run the first part of the tool, which is the generation of tests that invalidate specifications for each subject, do so as follows:

```bash
./experiments/run-experiment-pipeline.sh -m "L_Llama370Instruct_Q4" -p "General_V1"
```

Where `-m` specifies the models you want to use, and `-p` specifies the prompts to use based on the available prompts.
