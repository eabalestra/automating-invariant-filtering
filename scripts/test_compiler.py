import glob
import os
import subprocess

from pathlib import Path
from typing import List, Tuple

from scripts.code_extractor import get_java_package_name
from scripts.append_llm_tests import add_test_to_file

TEST_TEMPLATE = """
package {package};

import org.junit.Test;
import {subject_package}.*;

public class TestClass {{
}}
"""

TEMP_TEST_CLASS_NAME = "TestClass.java"
DEFAULT_CLASSPATH = "libs/junit-4.12.jar:."


class TestCompiler:
    def __init__(self, class_path: str, suite_path: str, method_name: str):
        self.class_path = Path(class_path)
        self.suite_path = Path(suite_path)
        self.method_name = method_name
        self.build_command = self._get_compilation_command()
        self._test_suite_package = None
        self._subject_package = None

    def is_test_compilable(self, test_code: str) -> Tuple[bool, str]:
        temp_file_path = None
        try:
            temp_file_path = self._create_temporary_test_file(test_code)
            compilation_success = self._compile_test_file(temp_file_path)
            return compilation_success, ""
        except Exception as e:
            return False, str(e)
        finally:
            if temp_file_path:
                self._cleanup_files(temp_file_path)

    def get_compilable_tests(self, test_candidates: List[str]) -> List[str]:
        compilable_tests = []
        total_tests = len(test_candidates)

        for test_code in test_candidates:
            is_compilable, _ = self.is_test_compilable(test_code)
            if is_compilable:
                compilable_tests.append(test_code)

        print(f"Found {len(compilable_tests)}/{total_tests} compilable tests")
        return compilable_tests

    def _get_compilation_command(self) -> List[str]:
        # current_path = self.class_path
        # while current_path != "/":
        #     if "gradlew" in os.listdir(current_path):
        #         print(f"Using Gradle for compilation in {current_path}")
        #         cmd = ['./gradlew', 'test', '--tests']
        #         return cmd
        #     current_path = current_path.parent
        return ['javac', '-cp', DEFAULT_CLASSPATH]

    def _create_temporary_test_file(self, test_code: str) -> str:
        test_template = self._get_test_template(
            self.test_suite_package,
            self.subject_package
        )
        temp_file_path = os.path.join(
            str(self.suite_path.parent),
            TEMP_TEST_CLASS_NAME
        )

        with open(temp_file_path, 'w', encoding='utf-8') as f:
            f.write(test_template)

        add_test_to_file(temp_file_path, test_code)
        return temp_file_path

    def _compile_test_file(self, test_file_path: str) -> bool:
        subject_files = self._get_subject_files()
        compilation_command = self.build_command + \
            subject_files + [test_file_path]

        success, error_msg = self._execute_compilation(compilation_command)
        return success

    def _execute_compilation(self, compilation_command: List[str]) -> Tuple[bool, str]:
        try:
            subprocess.run(
                compilation_command,
                check=True,
                capture_output=True,
                text=True
            )
            return True, ""
        except subprocess.CalledProcessError as e:
            print(f"{e.stderr}")
            return False, e.stderr
        except Exception as e:
            return False, str(e)

    def _get_subject_files(self) -> List[str]:
        return glob.glob(os.path.join(str(self.class_path.parent), '*.java'))

    @property
    def test_suite_package(self) -> str:
        if self._test_suite_package is None:
            self._test_suite_package = get_java_package_name(
                str(self.suite_path))
        return self._test_suite_package

    @property
    def subject_package(self) -> str:
        if self._subject_package is None:
            self._subject_package = get_java_package_name(str(self.class_path))
        return self._subject_package

    def _get_test_template(self, package: str, subject_package: str) -> str:
        return TEST_TEMPLATE.format(
            package=package,
            subject_package=subject_package
        )

    def _cleanup_files(self, *file_paths: str) -> None:
        for file_path in file_paths:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Failed to remove file {file_path}: {e}")
