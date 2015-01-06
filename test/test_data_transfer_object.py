# python -m unittest discover myproject/tests/ 'test*.py' myproject/

import unittest
import json

import sigma.data_transfer_object

class TestDataTransferObject(unittest.TestCase):
    """
    Test Data Transfer Object
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):

        raw_data_in = """
        [
            {
                "relative_key": [1, 1, 1],
                "absolute_key": [1.1, 1.1, 1.1],
                "value": [10]
            },
            {
                "relative_key": [2, 2, 2],
                "absolute_key": [2.2, 2.2, 2.2],
                "value": [20]
            },
            {
                "relative_key": [3, 3, 3],
                "absolute_key": [3.3, 3.3, 3.3],
                "value": [30]
            }
        ]
        """

        data_in = json.loads(raw_data_in)
        dto = sigma.data_transfer_object.DataTransferObjectConverter().assemble(data_in)
        data_out = sigma.data_transfer_object.DataTransferObjectConverter().disassemble(dto)
        raw_data_out = json.dumps(data_out)
