import os
import subprocess
import sys

subject_build_dir = sys.argv[1]

current_dir = os.getcwd()

os.chdir(subject_build_dir)

build_status = None
try:
    result = subprocess.run(
        ["./gradlew", "clean", "assemble", "testClasses", "-x", "test"],
        cwd=subject_build_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    build_status = result.returncode

    if result.returncode != 0:
        print(f"Error occurred while building {subject_build_dir}")
        print(f"Return code: {result.returncode}")
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)

except Exception as e:
    print(f"Exception occurred while building {subject_build_dir}: {e}")
    build_status = 1

os.chdir(current_dir)

if build_status != 0:
    sys.exit(1)
else:
    sys.exit(0)
