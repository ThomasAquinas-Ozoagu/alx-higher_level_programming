#!/usr/bin/python3
"""Unittest for islower(c)
"""
import unittest

islower = __import__('7-islower').islower


class TestIsLower(unittest.TestCase):
    """ This class will test my islower function
    """


    def test_islower(self):
        """ This method we confirm that the function works for all cases
        """
        self.assertTrue(islower('h'))
        self.assertFalse(islower('K'))

#if __name__ == '__main__':
#        unittest.main()
