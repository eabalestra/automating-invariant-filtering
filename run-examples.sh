echo "==> Running examples"
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not activated. Exiting."
    exit 1
fi

echo "==> Running example 1: getMin"

for specs in examples/simple-examples_getMin/specs/*; do
    echo "==> Running example $specs"
    sh run-automatic-invariant-filtering.sh examples/simple-examples_getMin/src/main/java/examples/SimpleMethods.java $specs getMin examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTester0.java
    mv examples/simple-examples_getMin/src/test/java/testers/SimpleMethodsTester0Augmented.java ../output/test/SimpleMethodsTester0Augmented${i}.java
    i=$((i+1))
done