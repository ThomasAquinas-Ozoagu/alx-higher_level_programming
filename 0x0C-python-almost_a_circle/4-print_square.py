#!/usr/bin/python3
"""
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the\
message size must be an integer
if size is less than 0, raise a ValueError exception with the message size\
must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the\
message size must be an integer
"""

def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        print("{}".format('#'*size))
