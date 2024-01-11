#!/usr/bin/python3
"""This module contains unittests for the BaseModel class"""

from models.base_model import BaseModel
import unittest


class TestInstanceType(unittest.TestCase):
    """Test the instance type"""

    def test_isinstance(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)


if __name__ == "__main__":
    unittest.main()
