import os
import subprocess

SUBJECTS_FILE = "experiments/subjects-to-run"

if not os.path.isfile(SUBJECTS_FILE):
    print(f"Error: {SUBJECTS_FILE} not found!")
    exit(1)

# Read subjects, skipping empty lines and comments
with open(SUBJECTS_FILE, "r") as f:
    subjects = [line.strip() for line in f if line.strip()
                and not line.strip().startswith("#")]

total_lines = len(subjects)
current_line = 0

for subject in subjects:
    current_line += 1
    percentage = current_line * 100 // total_lines

    args = subject.split()
    if len(args) < 3:
        print(f"Skipping invalid subject line: {subject}")
        continue

    class_name = args[1].split(".")[-1]
    test_suite = f"{class_name}Tester0"
    test_driver = f"{class_name}TesterDriver"

    print(
        f"Running tool with arguments: {args[0]}, {args[1]}, {args[2]}, {test_suite}, {test_driver}")
    print(f"Progress: {percentage}% ({current_line}/{total_lines})")

    cmd = ["./tool.sh", "--daikon-val-filter", args[0],
           args[1], args[2], test_suite, test_driver]
    subprocess.run(cmd)
