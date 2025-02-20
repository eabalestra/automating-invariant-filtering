import glob
import os
import subprocess
from typing import List

from utils import append_test_method_to_file, extract_package_path


def get_test_template(package: str, subject_package: str) -> str:
    return f"""
package {package};

import org.junit.Test;
import {subject_package}.*;

public class TestClass {{
}}
"""


def compile_java_files(javac_command: List[str]) -> bool:
    try:
        result = subprocess.run(
            javac_command,
            check=True,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


def cleanup_files(*file_paths: str) -> None:
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)


def check_if_test_compiles(test_suite_path: str, subject_path: str, test_method: str) -> bool:
    test_suite_package = extract_package_path(test_suite_path)
    test_suite_directory = os.path.dirname(test_suite_path)

    subject_dir = os.path.dirname(subject_path)
    subject_files = glob.glob(os.path.join(subject_dir, '*.java'))
    subject_package = extract_package_path(subject_path)

    test_template = get_test_template(test_suite_package, subject_package)
    new_test_path = os.path.join(test_suite_directory, 'TestClass.java')

    try:
        with open(new_test_path, 'w', encoding='utf-8') as f:
            f.write(test_template)
        append_test_method_to_file(new_test_path, test_method)

        javac_command = ['javac', '-cp', 'libs/junit-4.12.jar:.'] + \
            subject_files + [new_test_path]
        return compile_java_files(javac_command)
    finally:
        cleanup_files(new_test_path, os.path.join(
            test_suite_directory, 'TestClass.class'))
