import os
import re
import csv


def extract_test_counts(log_file):
    """
    Extract the number of generated and compiled tests from a log file.
    """
    generated_tests = 0
    compiled_tests = 0

    try:
        with open(log_file, 'r') as f:
            content = f.read()

            # Find the number of generated tests
            gen_match = re.search(r'Processing (\d+) tests from', content)
            if gen_match:
                generated_tests = int(gen_match.group(1))

            # Find the number of compiled tests
            comp_match = re.search(r'Compiled (\d+) tests', content)
            if comp_match:
                compiled_tests = int(comp_match.group(1))

        return generated_tests, compiled_tests

    except Exception as e:
        print(f"Error processing {log_file}: {str(e)}")
        return 0, 0


def extract_spec_counts(validation_log_file):
    """
    Extract the number of specifications in buckets and filtered specs from a validation log file.
    """
    specs_in_buckets = 0
    new_specs_filtered = 0

    try:
        with open(validation_log_file, 'r') as f:
            content = f.read()

            # Find the number of specs in buckets
            buckets_match = re.search(
                r'Specs from .*-buckets\.assertions: (\d+)', content)
            if buckets_match:
                specs_in_buckets = int(buckets_match.group(1))

            # Find the number of filtered specs
            filtered_match = re.search(
                r'Filtered specs: (\d+)', content)
            if filtered_match:
                new_specs_filtered = int(filtered_match.group(1))

        return specs_in_buckets, new_specs_filtered

    except Exception as e:
        print(
            f"Error processing validation log {validation_log_file}: {str(e)}")
        return 0, 0


def main():
    # Base output directory
    base_dir = "output"

    # List to store results
    results = []

    # Find all subject directories
    subject_dirs = [d for d in os.listdir(
        base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for subject in subject_dirs:
        # Path to the log files
        generated_tests_log_file = os.path.join(
            base_dir, subject, f"{subject}.log")
        validation_log_file = os.path.join(
            base_dir, subject, f"{subject}-second-round-validation.log")

        result = {
            "SUBJECT": subject,
            "generated-tests": 0,
            "compiled-tests": 0,
            "specs-in-buckets.assertions": 0,
            "new-specs-filtered": 0
        }

        if os.path.exists(generated_tests_log_file):
            generated, compiled = extract_test_counts(generated_tests_log_file)
            result["generated-tests"] = generated
            result["compiled-tests"] = compiled
        else:
            print(f"Test log file not found for {subject}")

        if os.path.exists(validation_log_file):
            specs_in_buckets, new_specs_filtered = extract_spec_counts(
                validation_log_file)
            result["specs-in-buckets.assertions"] = specs_in_buckets
            result["new-specs-filtered"] = new_specs_filtered
        else:
            print(f"Validation log file not found for {subject}")

        # Add the result even if one of the log files is missing
        results.append(result)

    if results:
        # Create results directory if it doesn't exist
        os.makedirs("experiments/results", exist_ok=True)

        # Write results to CSV
        csv_file = "experiments/results/test_generation_stats.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=["SUBJECT", "generated-tests", "compiled-tests",
                               "specs-in-buckets.assertions", "new-specs-filtered"])
            writer.writeheader()
            writer.writerows(results)

        print(f"Results written to {csv_file}")
        print("\nSummary:")
        print(f"Total subjects processed: {len(results)}")
        print(
            f"Total generated tests: {sum(r['generated-tests'] for r in results)}")
        print(
            f"Total compiled tests: {sum(r['compiled-tests'] for r in results)}")
        # total_generated = sum(r['generated-tests'] for r in results)
        # print(
        #     f"Average compilation rate: {sum(r['compiled-tests'] for r in results) / total_generated * 100:.2f}% (if tests were generated)" if total_generated > 0 else "Average compilation rate: 0.00% (no tests generated)")
        print(
            f"Total specs in buckets: {sum(r['specs-in-buckets.assertions'] for r in results)}")
        print(
            f"Total new specs filtered: {sum(r['new-specs-filtered'] for r in results)}")
    else:
        print("No results found")


if __name__ == "__main__":
    main()
