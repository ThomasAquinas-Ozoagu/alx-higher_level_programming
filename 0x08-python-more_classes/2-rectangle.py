#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Rectangle:
    """ This is an empty class, the methods/attributes will come later"""
    def __init__(self, width=0, height=0):
        """ This is an instantiation with optional values """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ This method returns the private attribute"""
        return self.__width

    @property
    def height(self):
        """ This method returns the private attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """ This method modifies the private attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ This method modifies the private attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
