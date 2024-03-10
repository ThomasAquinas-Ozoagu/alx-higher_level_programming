#!/usr/bin/python3
"""
Returns a list object
You are not allowed to import any module
"""


def lookup(obj):
    """
    a function that returns the list of available attributes and\
    methods of an object
    """
    return list(dir(obj))
