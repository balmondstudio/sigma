# python -m unittest discover myproject/tests/ 'test*.py' myproject/

import unittest

import sigma.component

class TestTemplate(unittest.TestCase):
    """
    Test Template
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        relative_key = [1, 1, 1]
        absolute_key = [1.0, 1.0, 1.0]
        value = [10]

        primitive = sigma.component.Primitive(relative_key, absolute_key, value)
        composite = sigma.component.Composite()
        composite.append(primitive)
