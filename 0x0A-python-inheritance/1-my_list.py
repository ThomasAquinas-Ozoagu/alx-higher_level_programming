#!/usr/bin/python3
"""
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """
    def __init__(self):
        """
        Initialize the parent class
        """
        super().__init__()

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        newlist = self[:]
        newlist.sort()
        print(newlist)
