# python -m unittest discover myproject/tests/ 'test*.py' myproject/

import unittest

import sigma.value_object

class TestValueObject(unittest.TestCase):
    """
    Test Value Object
    """

    def setUp(self):
        """Test setup."""
        pass

    def tearDown(self):
        """Test treardown."""
        pass

    def testIValueObject(self):
        """IValueObject class test."""

        a = sigma.value_object.IValueObject([1, 2, 3])
        b = sigma.value_object.IValueObject([1, 2, 3])

        self.assertEqual(a._data, [1, 2, 3])
        self.assertEqual(a.__repr__(), "IValueObject([1, 2, 3])")
        self.assertEqual(a.__str__(), "[1, 2, 3]")
        self.assertEqual(a.__bytes__(), b'\x01\x02\x03')
        self.assertEqual(a.__lt__(b), False)
        self.assertEqual(a.__gt__(b), False)
        self.assertEqual(a.__le__(b), True)
        self.assertEqual(a.__ge__(b), True)
        self.assertEqual(a.__eq__(b), True)
        self.assertEqual(a.__ne__(b), False)
        self.assertRaises(TypeError, lambda: a.__hash__())
        self.assertEqual(a.__bool__(), True)
        self.assertEqual(a.__add__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__radd__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__iadd__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__sub__(b), sigma.value_object.IValueObject([1, 2, 3]))
        self.assertEqual(a.__isub__(b), sigma.value_object.IValueObject([1, 2, 3]))
        self.assertEqual(a.__rsub__(b), sigma.value_object.IValueObject([0, 0, 0]))
        self.assertEqual(a.__mul__(b), sigma.value_object.IValueObject([1, 4, 9]))
        self.assertEqual(a.__rmul__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__imul__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__div__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rdiv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__idiv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__truediv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rtruediv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__itruediv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__floordiv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rfloordiv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__ifloordiv__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__mod__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rmod__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__imod__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__divmod__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rdivmod__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__pow__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rpow__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__ipow__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__lshift__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rlshift__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__ilshift__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rshift__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rrshift__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__irshift__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__and__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rand__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__iand__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__xor__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__rxor__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__ixor__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__or__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__ror__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__ior__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__neg__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__pos__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__abs__(b), sigma.value_object.IValueObject([2, 4, 6]))
        self.assertEqual(a.__invert__(b), sigma.value_object.IValueObject([2, 4, 6]))
        #TODO: a.__complex__()
        #TODO: a.__int__()
        #TODO: a.__float__()
        self.assertEqual(a.__round__(b), sigma.value_object.IValueObject([2, 4, 6]))
        #TODO: a.__index__()

    def testRelativeKey(self):
        """RelativeKey class test."""

        obj = sigma.value_object.RelativeKey(1, 2, 3)

        self.assertEqual(obj.i, 1)
        self.assertEqual(obj.j, 2)
        self.assertEqual(obj.k, 3)

    def testAbsoluteKey(self):
        """AbsoluteKey class test."""

        obj = sigma.value_object.AbsoluteKey(1, 2, 3)

        self.assertEqual(obj.x, 1)
        self.assertEqual(obj.y, 2)
        self.assertEqual(obj.z, 3)

    def testValue(self):
        """Value class test."""

        obj = sigma.value_object.Value(1)

        self.assertEqual(obj.value, [1])
