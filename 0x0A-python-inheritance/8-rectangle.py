#!/usr/bin/python3
""" Inheritance demonstration """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ Instantiation of Rectangle class """
        BaseGeometry.__init__(self)
        """self.__width = width
        self.__height = height"""

        def __width(self):
            self.integer_validator("width", width)
            self.__width = width

        def __height(self):
            self.integer_validator("height", height)
            self.__height = height
