# Automating Invariant Filtering

**Automating Invariant Filtering** is a tool ...

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Automatic Invariant Filtering](#automatic-invariant-filtering)
  - [Second Round Validation](#second-round-validation)
  - [Mutant Invariant Filtering](#mutant-invariant-filtering)
- [Example](#example)
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

   - Set the following environment variables to point to the corresponding directories:

   ```bash
   export DAIKONDIR=/path/to/daikon-5.8.2
   export SUBJECTS_DIR=/path/to/your/subjects
   export SPECS_DIR=/path/to/your/specs
   ```

   **Explanation:**

   - `DAIKONDIR`: The directory where Daikon is installed.
   - `SUBJECTS_DIR`: The directory containing the classes or subjects you wish to analyze.
   - `SPECS_DIR`: The directory where SpecFuzzer generated specifications will be stored.

3. **Create and Activate a Virtual Environment:**

   ```bash
      python3 -m venv venv
      source venv/bin/activate
   ```

4. **Install Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Models:**

   - Create the test generation model:

   ```bash
   ollama create test-generation-model -f testgen/Modelfile
   ```

   - Create the mutant generation model:

   ```bash
   ollama create mutant-generation-model -f mutgen/Modelfile
   ```

**Note:** Keep the models running while using the tool.

```bash
ollama run test-generation-model
```

## Usage

The tool consists of three main scripts, each serving a specific purpose in the invariant filtering process.

### Automatic Invariant Filtering

(explanation)

#### Command:

```bash
./run-automatic-invariant-filtering.sh <method_identifier> <class_name> <method_name> <test_class> <test_driver>
```

#### Parameters:

| Parameter             | Description                                                   |
| --------------------- | ------------------------------------------------------------- |
| `<method_identifier>` | Unique identifier for the method (e.g., `QueueAr_getFront`)   |
| `<class_name>`        | Short name of the class (e.g., `QueueAr`)                     |
| `<method_name>`       | Name of the method to analyze (e.g., `getFront`)              |
| `<test_class>`        | Associated test class or file (e.g., `QueueArTester0`)        |
| `<test_driver>`       | Driver or file to run the tests (e.g., `QueueArTesterDriver`) |

### Second Round Validation

(explanation)

```bash
./run-second-round-validation.sh <method_identifier> <fully_qualified_class_name> <method_name>
```

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

### Mutant Invariant Filtering

(explanation)

#### Command:

```bash
./run-mutant-invariant-filtering.sh <method_identifier> <fully_qualified_class_name> <method_name> <test_class> <test_driver>
```

#### Parameters:

| Parameter                      | Description                                          |
| ------------------------------ | ---------------------------------------------------- |
| `<method_identifier>`          | Unique method identifier (e.g., `Angle_getTurn`)     |
| `<fully_qualified_class_name>` | Fully qualified class name (e.g., `jts.Angle`)       |
| `<method_name>`                | Method name to analyze (e.g., `getTurn`)             |
| `<test_class> `                | Test class or file (e.g., `AngleTester0`)            |
| `<test_driver>`                | Driver file to run tests (e.g., `AngleTesterDriver`) |

## Example

Here’s a practical example using a hypothetical `QueueAr` class with the `getFront` method:

1. **Run Automatic Invariant Filtering:**

```bash
./run-automatic-invariant-filtering.sh QueueAr_getFront QueueAr getFront QueueArTester0 QueueArTesterDriver
```

2. **Run Second Round Validation:**

```bash
./run-second-round-validation.sh QueueAr_getFront DataStructures.QueueAr getFront
```

3. **Run Mutant Invariant Filtering:**

```bash
./run-mutant-invariant-filtering.sh QueueAr_getFront DataStructures.QueueAr getFront QueueArTester0 QueueArTesterDriver
```

## Notes

- Ensure models are running while executing the scripts.
- Verify environment variable paths if you encounter issues.
- For additional details on Ollama, visit the official [Ollama GitHub repository](https://github.com/ollama/ollama).
- Familiarity with [Specfuzzer](https://github.com/facumolina/specfuzzer) may enhance your understanding of this tool.