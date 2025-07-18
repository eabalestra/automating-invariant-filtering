# Automating Invariant Filtering

**Automating Invariant Filtering** is a tool designed to automatically filter and validate program invariants using Large Language Models (LLMs) and mutation testing techniques. This tool integrates with Daikon invariant detector and SpecFuzzer to enhance the precision of automatically generated specifications by filtering out false positives through targeted test generation.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Automatic Invariant Filtering](#automatic-invariant-filtering)
  - [Second Round Validation](#second-round-validation)
  - [Mutant Invariant Filtering](#mutant-invariant-filtering)
  - [Test-by-Test Invariant Analysis](#test-by-test-invariant-analysis)
- [Example](#example)
- [Output Structure](#output-structure)
- [Notes](#notes)

## Requirements

To use this tool, you will need:

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [Java 8](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html)
- [Ollama](https://ollama.com/) - A platform for running large language models locally.

## Installation

Follow these steps to set up the tool on your system:

1. **Download and Install Daikon:**

   - Download the specific version of Daikon required for this tool from [this link](https://mega.nz/file/pPgmnCST#dObECd8W5VeIDz5xzSgeQnhmH_-BRnOzt1VKaGn7Ihg).
   - Uncompress the downloaded file into a directory of your choice.

2. **Set Environment Variables:**

   You can either set the environment variables manually or use the provided setup script.

   **Option A: Use the Setup Script (Recommended)**
   
   ```bash
   source config/setup_env.sh
   ```

   **Option B: Manual Configuration**
   
   Set the following environment variables to point to the corresponding directories:

   ```bash
   export DAIKONDIR=/path/to/daikon-5.8.2
   export SUBJECTS_DIR=/path/to/your/subjects
   export SPECS_DIR=/path/to/your/specfuzzer-outputs
   export OPENAI_API_KEY=your_openai_api_key_here
   export API_KEY_HUGGINGFACE=your_huggingface_api_key_here
   export GOOGLE_API_KEY=your_google_api_key_here
   ```

   **Explanation:**

   - `DAIKONDIR`: The directory where Daikon is installed.
   - `SUBJECTS_DIR`: The directory containing the classes or subjects you wish to analyze (typically contains Maven/Gradle projects with src/main/java and src/test/java structure).
   - `SPECS_DIR`: The directory where SpecFuzzer generated specifications will be stored.
   - `OPENAI_API_KEY`: Your OpenAI API key for LLM-based test generation (optional, if using OpenAI models).
   - `API_KEY_HUGGINGFACE`: Your Hugging Face API key for accessing HuggingFace models (optional).
   - `GOOGLE_API_KEY`: Your Google API key for accessing Google's LLM services (optional).

3. **Create and Activate a Virtual Environment:**

   ```bash
      python3 -m venv venv
      source venv/bin/activate
   ```

4. **Install Python Dependencies:**

   ```bash
   pip install -r config/requirements.txt
   ```

## Usage

The tool consists of four main scripts, each serving a specific purpose in the invariant filtering process.

### Automatic Invariant Filtering

This script takes all specifications found in the `-buckets.assertion` file generated by SpecFuzzer and attempts to generate tests using Large Language Models (LLMs) for each specification. The generated tests are then added to the existing test suite (including the one generated by SpecFuzzer) to create an augmented test suite for validation.

#### Command:

```bash
./run-automatic-invariant-filtering.sh <method_identifier> <fully_qualified_class_name> <method_name> -models "L_Llama318Instruct" -p "General_V1"
```

#### Parameters:

| Parameter                      | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `<method_identifier>`          | Unique identifier for the method (e.g., `QueueAr_getFront`) |
| `<fully_qualified_class_name>` | Fully qualified class name (e.g., `DataStructures.QueueAr`) |
| `<method_name>`                | Name of the method to analyze (e.g., `getFront`)            |
| `-models`                      | LLM models to use for test generation                       |
| `-p`                           | Prompt version to use                                       |

#### Process:

1. Extracts specifications from SpecFuzzer output
2. Generates test cases using specified LLM models
3. Compiles and validates generated tests
4. Augments existing test suite with new tests

### Second Round Validation

This script takes the augmented test suite (containing both SpecFuzzer-generated tests and new LLM-generated tests) and runs Daikon to determine which specifications are filtered out by the enhanced test suite.

#### Command:

```bash
./run-second-round-validation.sh <method_identifier> <fully_qualified_class_name> <method_name>
```

#### Parameters:

| Parameter                      | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `<method_identifier>`          | Unique identifier for the method (e.g., `QueueAr_getFront`) |
| `<fully_qualified_class_name>` | Fully qualified class name (e.g., `DataStructures.QueueAr`) |
| `<method_name>`                | Method name to analyze (e.g., `getFront`)                   |

#### Process:

1. Uses the augmented test suite from the previous step
2. Runs Daikon dynamic analysis
3. Compares original specifications with those surviving the enhanced test suite
4. Reports filtered (invalid) specifications

<!-- ### Mutant Invariant Filtering

This script performs mutation-based validation of invariants by generating mutants of the target class and checking which specifications are violated by the mutated versions.

#### Command:

```bash
./run-mutant-invariant-filtering.sh <subject_name> <fully_qualified_class_name> <method_name> <test_suite_name> <test_driver_name>
```

#### Parameters:

| Parameter                      | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `<subject_name>`               | Name of the subject/project                                 |
| `<fully_qualified_class_name>` | Fully qualified class name (e.g., `DataStructures.QueueAr`) |
| `<method_name>`                | Method name to analyze                                       |
| `<test_suite_name>`            | Name of the test suite class                                |
| `<test_driver_name>`           | Name of the test driver class                               |

#### Process:
1. Generates code mutations for the target class
2. Compiles and tests each mutant
3. Runs Daikon on mutant executions
4. Identifies specifications that remain valid across mutants (potential false positives)

### Test-by-Test Invariant Analysis

This script analyzes which specifications are filtered by each individual test in the test suite, providing detailed insights into the contribution of each test case.

#### Command:

```bash
./run-test-by-test-invariant-analysis.sh <subject_name> <fully_qualified_class_name> <method_name>
```

#### Parameters:

| Parameter                      | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `<subject_name>`               | Name of the subject/project                                 |
| `<fully_qualified_class_name>` | Fully qualified class name (e.g., `DataStructures.QueueAr`) |
| `<method_name>`                | Method name to analyze                                       |

#### Process:
1. Extracts individual tests from the test suite
2. Runs Daikon analysis for each test separately
3. Determines which specifications each test filters
4. Generates per-test analysis reports -->

## Example

Here's a complete example of using the tool to analyze the `getFront` method of a `QueueAr` class:

```bash
# Step 1: Run automatic invariant filtering with LLM test generation
./run-automatic-invariant-filtering.sh QueueAr_getFront DataStructures.QueueAr getFront -models "L_Llama318Instruct" -p "General_V1"

# Step 2: Validate the filtered specifications with the enhanced test suite
./run-second-round-validation.sh QueueAr_getFront DataStructures.QueueAr getFront
```

<!--
# Step 3: (Optional) Run mutation-based validation
./run-mutant-invariant-filtering.sh QueueAr DataStructures.QueueAr getFront QueueArTester0 QueueArTesterDriver

# Step 4: (Optional) Analyze contribution of individual tests
./run-test-by-test-invariant-analysis.sh QueueAr DataStructures.QueueAr getFront -->

## Output Structure

The tool generates organized output in the `output/` directory:

```
output/
└── <ClassName>_<MethodName>/
    ├── <ClassName>_<MethodName>.log              # Main execution log
    ├── <ClassName>_<MethodName>-second-round-validation.log  # Validation log
    ├── test/
    │   ├── <ClassName>_<MethodName>LlmTest.java          # Generated LLM tests
    │   ├── <ClassName>_<MethodName>LlmFixedTest.java     # Fixed LLM tests
    │   ├── <ClassName>_<MethodName>LlmCompilableTest.java # Compilable tests
    │   └── specs_per_test/                               # Per-test analysis
    │       ├── test001-invs.csv
    │       ├── test002-invs.csv
    │       └── ...
    ├── specs/
    │   ├── interest-specs.csv                    # Specifications of interest
    │   ├── non-filtered-specs.csv               # Specifications that survived
    │   └── filtered-specs.csv                   # Filtered specifications
    ├── mutations/                                # Mutation testing results
    │   ├── compiled-mutations.txt
    │   ├── generated-mutations.txt
    │   ├── mutants/
    │   └── mutants-traces/
    └── daikon/                                   # Daikon analysis outputs
        ├── objects.xml
        ├── trace.dtrace.gz
        └── ...
```

## Notes

### Prerequisites

- Ensure Ollama models are running before executing LLM-based scripts
- Verify all environment variable paths are correctly set
- Make sure the target Java project is properly compiled with test suites generated by SpecFuzzer

### Tool Integration

- This tool is designed to work with [SpecFuzzer](https://github.com/facumolina/specfuzzer) output
- Compatible with [Daikon](https://plse.cs.washington.edu/daikon/) version 5.8.2
- Integrates with [Ollama](https://ollama.com/) for local LLM execution

### Troubleshooting

- If you encounter compilation issues, check that all required dependencies are in the classpath
- For LLM-related errors, ensure the specified models are available in Ollama
- Verify that the subject directory structure follows the expected Maven/Gradle layout

### Research Context

This tool supports research in automated specification mining and validation, particularly focused on:

- Reducing false positives in automatically generated invariants
- Leveraging LLMs for targeted test case generation
- Mutation-based validation of program specifications
- Understanding the contribution of individual test cases to specification filtering

For additional details on the underlying technologies:

- [Ollama GitHub repository](https://github.com/ollama/ollama)
- [Daikon documentation](https://plse.cs.washington.edu/daikon/)
- [SpecFuzzer repository](https://github.com/facumolina/specfuzzer)
