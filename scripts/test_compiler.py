import os
import subprocess

from utils import append_test_method_to_file, extract_package_path


def get_test_template(package: str) -> str:
    return f"""
package {package};

import org.junit.Test;

public class TestClass {{
}}
"""


def check_if_test_compiles(test_suite_path: str, subject_path: str, test_method: str) -> bool:
    package = extract_package_path(test_suite_path)
    path = os.path.dirname(test_suite_path)
    test_template = get_test_template(package)
    new_test_path = f'{path}/TestClass.java'
    try:
        with open(new_test_path, 'w', encoding='utf-8') as f:
            f.write(test_template)
        append_test_method_to_file(new_test_path, test_method)
        result = subprocess.run(
            ['javac', '-cp', 'libs/junit-4.12.jar:.', subject_path, new_test_path],
            check=True,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e.stderr}")
        return False
    finally:
        if os.path.exists(new_test_path):
            os.remove(new_test_path)
        if os.path.exists(f'{path}/TestClass.class'):
            os.remove(f'{path}/TestClass.class')
