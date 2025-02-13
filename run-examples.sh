echo "==> Running examples"
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment not activated. Exiting."
    exit 1
fi
echo "=> Example 1: Sorted List: insert(int data)"
python search-counterexample.py examples/DataStructuresList_insert/List.java examples/DataStructuresList_insert/slist-specs.csv insert
echo "=> Example 2: StackAr_topAndPop"
python search-counterexample.py examples/StackAr_topAndPop/StackAr.java examples/StackAr_topAndPop/stack-specs.csv topAndPop
echo "=> Example 3: simple-examples_getMin"
python search-counterexample.py examples/simple-examples_getMin/SimpleMethods.java examples/simple-examples_getMin/simple-methods-specs.csv getMin
# echo "=> Example 4: "
# python search-counterexample.py 