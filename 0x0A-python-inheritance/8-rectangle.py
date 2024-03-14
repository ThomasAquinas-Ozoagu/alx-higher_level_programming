#!/usr/bin/python3
""" Inheritance demonstration """


class BaseGeometry:
    """ This class will be used to practice how to display default
    class parameters'
    """

    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the variable VALUE, whose name is a STRING """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ Instantiation of Rectangle class """
        super().__init__()

    def __width(self):
        self.integer_validator("width", width)
        __width = width

    def __height(self):
        self.integer_validator("height", height)
        __height = height
