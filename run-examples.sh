echo "==> Running examples"
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not activated. Exiting."
    exit 1
fi

echo "==> Running example 2: clamp"
i=0
for specs in examples/MathUtil_clamp/specs/*; do
    echo "==> Running example $specs"
    sh run-automatic-invariant-filtering.sh examples/MathUtil_clamp/src/main/java/jts/MathUtil.java $specs clamp examples/MathUtil_clamp/src/test/java/testers/MathUtilTester0.java examples/MathUtil_clamp/src/test/java/testers/MathUtilTesterDriver.java
    augmented_file="examples/MathUtil_clamp/src/test/java/testers/MathUtilTester0Augmented.java"
    test_driver="examples/MathUtil_clamp/src/test/java/testers/MathUtilTesterDriver.java"
    if [ -f "$augmented_file" ]; then
        mv "$augmented_file" "output/test/MathUtil_clamp/MathUtilTester0Augmented-${i}.java"
        mv "$test_driver" "output/test/MathUtil_clamp/MathUtilTesterDriverAugmented-${i}.java"
        i=$((i + 1))
    else
        echo "File $augmented_file does not exist. Skipping."
    fi
done

echo "==> Running example 1: getMin"
i=0
for specs in examples/simple-examples_getMin/specs/*; do
    echo "==> Running example $specs"
    sh run-automatic-invariant-filtering.sh examples/simple-examples_getMin/src/main/java/examples/SimpleMethods.java $specs getMin examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTester0.java examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTesterDriver.java
    augmented_file="examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTester0Augmented.java"
    test_driver="examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTesterDriverAugmented.java"
    if [ -f "$augmented_file" ]; then
        mv "$augmented_file" "output/test/SimpleMethods/SimpleMethodsTester0Augmented-${i}.java"
        mv "$test_driver" "output/test/SimpleMethods/SimpleMethodsTesterDriverAugmented-${i}.java"
        i=$((i + 1))
    else
        echo "File $augmented_file does not exist. Skipping."
    fi
done
