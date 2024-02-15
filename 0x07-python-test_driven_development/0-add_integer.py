#!/usr/bin/python3
"""
Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception 
with the message a must be an integer or b must be an integer
"""
def add_integer(a, b=98):
    """ a function that adds 2 integers 
    a and b must be first casted to integers if they are float
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return (a + b)
