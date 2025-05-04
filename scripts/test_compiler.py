import glob
import os
import subprocess
from typing import List, Tuple

from code_extractor import extract_package_path
from append_llm_tests import append_test_method_to_file


def get_test_template(package: str, subject_package: str) -> str:
    return f"""
package {package};

import org.junit.Test;
import {subject_package}.*;

public class TestClass {{
}}
"""


def compile_java_files(javac_command: List[str]) -> Tuple[bool, str]:
    try:
        result = subprocess.run(
            javac_command,
            check=True,
            capture_output=True,
            text=True
        )
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def cleanup_files(*file_paths: str) -> None:
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)


def find_jar_files(base_dir: str) -> List[str]:
    """Find all jar files in the project that might be useful for compilation."""
    jar_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.jar'):
                jar_files.append(os.path.join(root, file))
    return jar_files


def find_project_root(file_path: str) -> str:
    """Find the project root directory by looking for build files up the directory tree."""
    current_dir = os.path.dirname(os.path.abspath(file_path))
    while current_dir != "/" and current_dir:
        # Check for common build system indicators
        if (os.path.exists(os.path.join(current_dir, "build.gradle")) or
            os.path.exists(os.path.join(current_dir, "pom.xml")) or
            os.path.exists(os.path.join(current_dir, "gradlew")) or
                os.path.exists(os.path.join(current_dir, "mvnw"))):
            return current_dir
        current_dir = os.path.dirname(current_dir)

    # If no build files found, return the directory of the file
    return os.path.dirname(os.path.abspath(file_path))


def check_if_test_compiles(test_suite: str, subject_class: str, unit_test: str) -> Tuple[bool, str]:
    test_suite_package = extract_package_path(test_suite)
    test_suite_directory = os.path.dirname(test_suite)
    subject_dir = os.path.dirname(subject_class)
    subject_files = glob.glob(os.path.join(subject_dir, '*.java'))
    subject_package = extract_package_path(subject_class)

    test_template = get_test_template(test_suite_package, subject_package)
    new_test_path = os.path.join(test_suite_directory, 'TestClass.java')

    try:
        with open(new_test_path, 'w', encoding='utf-8') as f:
            f.write(test_template)
        append_test_method_to_file(new_test_path, unit_test)

        # Find the project root by looking at both the subject class and test suite paths
        project_root_from_subject = find_project_root(subject_class)
        project_root_from_test = find_project_root(test_suite)

        # Use the "highest" directory (closest to root) as this is more likely to contain build files
        if len(project_root_from_subject) <= len(project_root_from_test):
            project_root = project_root_from_subject
        else:
            project_root = project_root_from_test

        print(f"Project root detected: {project_root}")

        # Store current working directory to restore it later
        original_dir = os.getcwd()

        # Change directory to project root for build commands
        os.chdir(project_root)

        try:
            if os.path.exists('gradlew') or os.path.exists('build.gradle'):
                print("Gradle build detected")
                cmd = ['./gradlew' if os.path.exists('gradlew') else 'gradle', 'test',
                       '--tests', f"{test_suite_package}.TestClass"]
                try:
                    result = subprocess.run(
                        cmd, check=True, capture_output=True, text=True)
                    return True, ""
                except subprocess.CalledProcessError as e:
                    return False, e.stderr

            elif os.path.exists('mvnw') or os.path.exists('pom.xml'):
                print("Maven build detected")
                cmd = ['./mvnw' if os.path.exists('mvnw') else 'mvn', 'test',
                       '-Dtest=TestClass']
                try:
                    result = subprocess.run(
                        cmd, check=True, capture_output=True, text=True)
                    return True, ""
                except subprocess.CalledProcessError as e:
                    return False, e.stderr

            else:
                print("No build system detected, using default classpath")
                jar_files = find_jar_files(project_root)
                classpath_elements = ['libs/junit-4.12.jar', '.'] + jar_files
                classpath = ':'.join(classpath_elements) if os.name != 'nt' else ';'.join(
                    classpath_elements)

                javac_command = ['javac', '-cp', classpath] + \
                    subject_files + [new_test_path]
                return compile_java_files(javac_command)
        finally:
            # Restore original directory
            os.chdir(original_dir)
    finally:
        cleanup_files(new_test_path, os.path.join(
            test_suite_directory, 'TestClass.class'))


def get_compilable_tests(compilation_target_suite: str, target_class: str, test_candidates: List[str]) -> List[str]:
    compiled_tests = []
    for i, test in enumerate(test_candidates):
        success, error_msg = check_if_test_compiles(
            compilation_target_suite, target_class, test)
        if success:
            compiled_tests.append(test)
        else:
            print(f"Test {i+1} failed to compile with error:\n{error_msg}")
    return compiled_tests
