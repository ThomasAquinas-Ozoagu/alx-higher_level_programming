#!/usr/bin/python3
""" Inheritance demonstration """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ Instantiation of Rectangle class """
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
