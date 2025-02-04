echo "==> Running examples"
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not activated. Exiting."
    exit 1
fi
echo "=> Example 1: Multiplication: multiply(int a, int b)"
python main.py examples/ArithmeticUtils/Multiplier.java examples/ArithmeticUtils/multiply_specs.csv multiply
echo "=> Example 2: Sorted List: insert(int data)"
python main.py examples/DataStructuresList_insert/List.java examples/DataStructuresList_insert/slist-specs.csv insert
echo "=> Example 3: StackAr: topAndPop()"
python main.py examples/StackAr_topAndPop/StackAr.java examples/StackAr_topAndPop/stack-specs.csv topAndPop