#!/usr/bin/python3
"""Unittest for pow(a, b)
"""
import unittest

pow = __import__('11-pow').pow


class Pow(unittest.TestCase):
    """ This class will test my pow function
    """


    def test_pow(self):
        """ This method we confirm that the function works for all cases
        """
        self.assertEqual(pow(2, 2), 4)
        self.assertEqual(pow(98, 2), 9604)
        self.assertEqual(pow(98, 0), 1)
        self.assertEqual(pow(100, -2), 0.0001)
        self.assertEqual(pow(-4, 5), -1024)
