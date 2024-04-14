#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class will test my Max integer code
    """

    def test_max(self):
        """ This method will assert equality on the result
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1, 2, 0, -4]), 2)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
