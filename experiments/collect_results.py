import os
import re
import csv
import glob


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


def main():
    # Base output directory
    base_dir = "output"

    # List to store results
    results = []

    # Find all subject directories
    subject_dirs = [d for d in os.listdir(
        base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    for subject in subject_dirs:
        # Path to the log file
        generated_tests_log_file = os.path.join(base_dir, subject, f"{subject}.log")

        if os.path.exists(generated_tests_log_file):
            generated, compiled = extract_test_counts(generated_tests_log_file)
            results.append({
                "SUBJECT": subject,
                "generated-tests": generated,
                "compiled-tests": compiled
            })
        else:
            print(f"Log file not found for {subject}")

    if results:
        # Create results directory if it doesn't exist
        os.makedirs("experiments/results", exist_ok=True)

        # Write results to CSV
        csv_file = "experiments/results/test_generation_stats.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=["SUBJECT", "generated-tests", "compiled-tests"])
            writer.writeheader()
            writer.writerows(results)

        print(f"Results written to {csv_file}")
        print("\nSummary:")
        print(f"Total subjects processed: {len(results)}")
        print(
            f"Total generated tests: {sum(r['generated-tests'] for r in results)}")
        print(
            f"Total compiled tests: {sum(r['compiled-tests'] for r in results)}")
        total_generated = sum(r['generated-tests'] for r in results)
        print(
            f"Average compilation rate: {sum(r['compiled-tests'] for r in results) / total_generated * 100:.2f}% (if tests were generated)" if total_generated > 0 else "Average compilation rate: 0.00% (no tests generated)")
    else:
        print("No results found")


if __name__ == "__main__":
    main()
