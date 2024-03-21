#!/usr/bin/python3
""" Integer validator """


class BaseGeometry:
    """ This class will be used to practice how to display default
    class parameters'
    """
    def __init__(self):
        """ An empty init, class has no variables yet """
        pass

    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the variable VALUE, whose name is a STRING """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
