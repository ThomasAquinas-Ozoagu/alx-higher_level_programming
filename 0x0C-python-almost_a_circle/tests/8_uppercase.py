#!/usr/bin/python3
"""Unittest for uppercase(str)
"""
import unittest

uppercase = __import__('8-uppercase').uppercase


class TestUpperCase(unittest.TestCase):
    """ This class will test my uppercase function
    """


    def test_uppercase(self):
        """ This method we confirm that the function works for all cases
        """
        self.assertEqual(uppercase("Best School 98 Battery street"),
                         "BEST SCHOOL 98 BATTERY STREET")
        self.assertEqual(uppercase("end"), "END")
