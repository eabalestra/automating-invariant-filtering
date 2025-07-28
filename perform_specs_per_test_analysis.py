import os
import sys
import csv
from pathlib import Path


def extract_specs(file_path):
    """Extract specs from a file, ignoring unwanted lines."""
    specs = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(("orig_specs=", "filtered_specs=")):
                continue
            specs.add(line)
    return specs


def generate_csv(folder_path, output_csv="specs_matrix.csv"):
    """Generate a CSV where rows=specs, columns=files, and cells=1/0."""
    all_files = list(Path(folder_path).glob("*.txt"))  # Only .txt files
    file_names = [f.stem for f in all_files]  # Remove .txt
    all_specs = set()

    # Step 1: Compute union of all specs across files
    for file in all_files:
        all_specs.update(extract_specs(file))
    all_specs = sorted(all_specs)  # Sort for readability

    # Step 2: Build a {spec: {file: 1/0}} mapping
    spec_matrix = {}
    for spec in all_specs:
        spec_matrix[spec] = {}
        for file in all_files:
            file_specs = extract_specs(file)
            spec_matrix[spec][file.stem] = 1 if spec in file_specs else 0

    # Step 3: Write to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Header: "Specification", "llmTest1", "llmTest2", ...
        writer.writerow(["Specification"] + file_names)
        # Rows: Each spec followed by 1/0s
        for spec in all_specs:
            row = [spec] + [spec_matrix[spec][name] for name in file_names]
            writer.writerow(row)

    print(f"CSV generated at: {output_csv}")


# Usage
folder_path = sys.argv[1]
generate_csv(folder_path)
