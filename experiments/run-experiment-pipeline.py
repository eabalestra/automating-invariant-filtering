#!/usr/bin/env python3
"""
Experiment pipeline for running automatic invariant filtering and
second round validation. This Python version provides better error handling
and process management than the bash version.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def setup_environment():
    """Setup the environment by sourcing the config and activating venv."""
    # Change to the project root directory
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    # Source the environment setup (we'll use environment variables directly)
    # The bash script sources config/setup_env.sh and venv/bin/activate
    # We'll assume the environment is already set up or set it programmatically

    # Activate virtual environment if it exists
    venv_python = project_root / "venv" / "bin" / "python3"
    if venv_python.exists():
        # We're already running in Python, so we'll use subprocess for
        # external commands
        pass

    return project_root


def run_command(command, description, continue_on_error=True, dry_run=False):
    """
    Run a shell command and return success status.

    Args:
        command: List of command arguments or string command
        description: Description of what the command does
        continue_on_error: Whether to continue if the command fails
        dry_run: If True, just print what would be executed

    Returns:
        bool: True if command succeeded, False otherwise
    """
    try:
        print(f"> {description}")

        if dry_run:
            if isinstance(command, str):
                print(f"[DRY RUN] Would execute: {command}")
            else:
                print(f"[DRY RUN] Would execute: {' '.join(command)}")
            return True

        if isinstance(command, str):
            result = subprocess.run(
                command, shell=True, check=False, capture_output=False, text=True
            )
        else:
            result = subprocess.run(
                command, check=False, capture_output=False, text=True
            )

        if result.returncode == 0:
            print(f"✓ {description} completed successfully")
            return True
        else:
            print(f"✗ {description} failed with exit code {result.returncode}")
            if not continue_on_error:
                sys.exit(result.returncode)
            return False

    except Exception as e:
        print(f"✗ {description} failed with exception: {e}")
        if not continue_on_error:
            sys.exit(1)
        return False


def read_subjects_file(subjects_file):
    """Read and parse the subjects file, filtering out comments."""
    subjects = []

    if not subjects_file.exists():
        print(f"Error: {subjects_file} not found!")
        sys.exit(1)

    with open(subjects_file, "r") as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith("#"):
                subjects.append(line.split())

    return subjects


def main():
    """Main pipeline execution."""
    # Default values
    DEFAULT_MODELS = "L_Llama318Instruct, L_Mistral7B03Instruct, " "L_Phi4_Q4"
    DEFAULT_PROMPTS = "General_V1"

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run experiment pipeline")
    parser.add_argument(
        "-m",
        "--models",
        default=DEFAULT_MODELS,
        help=f"Models to use (default: {DEFAULT_MODELS})",
    )
    parser.add_argument(
        "-p",
        "--prompts",
        default=DEFAULT_PROMPTS,
        help=f"Prompts to use (default: {DEFAULT_PROMPTS})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be executed without running it",
    )

    args = parser.parse_args()

    # Setup environment
    project_root = setup_environment()

    # Path to the file containing the list of subjects
    subjects_file = project_root / "experiments" / "subjects-to-run"

    # Read subjects
    subjects = read_subjects_file(subjects_file)
    total_subjects = len(subjects)

    print("> Running experiment pipeline with the following configuration:")
    print(f"Models: {args.models}")
    print(f"Prompts: {args.prompts}")
    print(f"Subjects file: {subjects_file}")
    print(f"Total subjects to process: {total_subjects}")
    print("")

    # Process each subject
    for i, subject_args in enumerate(subjects, 1):
        if len(subject_args) < 3:
            print(f"✗ Skipping invalid subject line: {' '.join(subject_args)}")
            continue

        subject_name = subject_args[0]
        class_name = subject_args[1]
        method_name = subject_args[2]

        # Calculate progress
        percentage = (i * 100) // total_subjects

        print(
            f"Running tool with arguments: {subject_name}, "
            f"{class_name}, {method_name}"
        )
        print(f"Progress: {percentage}% ({i}/{total_subjects})")
        print("")

        # Run automatic invariant filtering
        cmd1 = [
            "./run-automatic-invariant-filtering.sh",
            subject_name,
            class_name,
            method_name,
            "-m",
            args.models,
            "-p",
            args.prompts,
        ]

        success1 = run_command(
            cmd1,
            f"Automatic invariant filtering for "
            f"{subject_name} {class_name} {method_name}",
            continue_on_error=True,
            dry_run=args.dry_run,
        )

        if success1:
            print(
                f"✓ Automatic invariant filtering completed successfully "
                f"for {subject_name} {class_name} {method_name}"
            )
        else:
            print(
                f"✗ Automatic invariant filtering failed for "
                f"{subject_name} {class_name} {method_name} - "
                f"continuing with next subject"
            )

        print("")

        # Run second round validation
        cmd2 = [
            "./run-second-round-validation.sh",
            subject_name,
            class_name,
            method_name,
        ]

        success2 = run_command(
            cmd2,
            f"Second round validation for "
            f"{subject_name} {class_name} {method_name}",
            continue_on_error=True,
            dry_run=args.dry_run,
        )

        if success2:
            print(
                f"✓ Second round validation completed successfully "
                f"for {subject_name} {class_name} {method_name}"
            )
        else:
            print(
                f"✗ Second round validation failed for "
                f"{subject_name} {class_name} {method_name} - "
                f"continuing with next subject"
            )

        print("")
        print("-" * 80)
        print("")

    # Collect results after processing all subjects
    print("Collecting results...")
    success_collect = run_command(
        ["python3", "experiments/collect_results.py"],
        "Collecting results",
        continue_on_error=False,
        dry_run=args.dry_run,
    )

    if success_collect:
        print("")
        print("Done! All SpecFuzzer's subjects processed.")
        print("Results saved to experiments/results/test_generation_stats.csv")
    else:
        print("Failed to collect results.")
        sys.exit(1)


if __name__ == "__main__":
    main()
