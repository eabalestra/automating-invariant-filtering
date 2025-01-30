from testgen import test_generator

cls = 'Multiplier'
info = '''
Multiplier()
multiply(int a, int b)
Method: public int multiply(int x, int y) {
    return x * y;
}'''
likely_valid_specs = ['x >= result && y >= result']

for spec in likely_valid_specs:
    test_generator.generate_test(cls, info, spec)
