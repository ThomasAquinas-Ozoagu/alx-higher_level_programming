#!/usr/bin/python3
"""Unittest for print_last_digit(number)
"""
import unittest

print_last_digit = __import__('9-print_last_digit').print_last_digit


class PrintLastDigit(unittest.TestCase):
    """ This class will test my print_last_digit function
    """


    def test_print_last_digit(self):
        """ This method we confirm that the function works for all cases
        """
        self.assertEqual(print_last_digit(98), 8)
        self.assertEqual(print_last_digit(0), 0)
        self.assertEqual(print_last_digit(-1024), 4)
