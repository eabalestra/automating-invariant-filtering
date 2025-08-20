import os
import subprocess
import sys

subject_build_dir = sys.argv[1]

current_dir = os.getcwd()

os.chdir(subject_build_dir)

result = subprocess.run(
    ["./gradlew", "clean", "-q", "-Dskip.tests", "jar"],
    stdin=subprocess.DEVNULL,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)

build_status = result.returncode

os.chdir(current_dir)

if build_status != 0:
    sys.exit(1)
else:
    sys.exit(0)
