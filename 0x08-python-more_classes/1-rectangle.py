#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Rectangle:
    """ This is an empty class, the methods/attributes will come later"""
    def __init__(self, width=0, height=0):
        """ This is an instantiation with optional values """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ This method returns the private attribute"""
            return self.__width

        @width.setter
        def width(self, width):
            """ This method modifies the private attribute"""
            if type(width) != int:
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width

        @property
        def height(self):
            """ This method returns the private attribute"""
            return self.__height

        @height.setter
        def height(self, height):
            """ This method modifies the private attribute"""
            if type(height) != int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
