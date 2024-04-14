#!/usr/bin/python3
"""Unittest for add(a, b)
"""
import unittest

add = __import__('10-add').add


class Add(unittest.TestCase):
    """ This class will test my print_last_digit function
    """


    def test_add(self):
        """ This method we confirm that the function works for all cases
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(98, 0), 98)
        self.assertEqual(add(100, -2), 98)
