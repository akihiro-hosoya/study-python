class TestClass:

    def __init__(self):
        print('create TestClass')

    def test_method(self, val):
        print('call test_method')
        print(val)



import testmod

test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

from testmod import TestClass

test_class_2 = TestClass()
test_class_2.test_method('2')