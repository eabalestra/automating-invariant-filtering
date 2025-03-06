import subprocess
import os
import sys

cp_for_daikon = sys.argv[1]
driver_package = sys.argv[2]
mutant_driver = sys.argv[3]
mutant_dir = sys.argv[4]
driver_base = sys.argv[5]
i = sys.argv[6]

print(
    f"> Performing Dynamic Comparability Analysis from driver: {driver_package}.{mutant_driver}")

dyncomp_cmd = [
    "java",
    "-cp", cp_for_daikon,
    "daikon.DynComp",
    f"{driver_package}.{mutant_driver}",
    "--output-dir=" + os.path.join(mutant_dir, "daikon")
]
subprocess.run(dyncomp_cmd)

print('> Generating traces with Chicory from mutant')
cmp_file = os.path.join(mutant_dir, "daikon", f"{mutant_driver}.decls-DynComp")
mutant_driver_base = f"{driver_base}Mutant{i}"

chicory_cmd = [
    "java",
    "-cp", cp_for_daikon,
    "daikon.Chicory",
    "--output-dir=daikon-outputs/mutants",
    "--comparability-file=" + cmp_file,
    "--ppt-omit-pattern=" + mutant_driver_base + ".*",
    "--ppt-omit-pattern=org.junit.*",
    "--dtrace-file=" + f"{mutant_driver}-m{i}.dtrace.gz",
    f"{driver_package}.{mutant_driver}",
    "daikon-outputs/mutants/" + f"{mutant_driver}-m{i}-objects.xml"
]

subprocess.run(chicory_cmd,
               stdin=subprocess.DEVNULL,
               stdout=subprocess.DEVNULL,
               stderr=subprocess.DEVNULL)
