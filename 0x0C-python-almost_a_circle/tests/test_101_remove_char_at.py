#!/usr/bin/python3
"""Unittest for remove_char_at(str, n)
"""
import unittest

remove_char_at = __import__('101-remove_char_at').remove_char_at


class RemoveCharAt(unittest.TestCase):
    """ This class will test my remove_char_at function
    """


    def test_remove_char_at(self):
        """ This method we confirm that the function works for all cases
        """
        self.assertEqual(remove_char_at("Best School", 3), "Bes School")
        self.assertEqual(remove_char_at("Chicago", 2), "Chcago")
        self.assertEqual(remove_char_at("C is fun!", 0), " is fun!")
        self.assertEqual(remove_char_at("School", 10), "School")
        self.assertEqual(remove_char_at("Python", -2), "Python")
