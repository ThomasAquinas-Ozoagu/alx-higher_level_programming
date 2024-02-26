#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Rectangle:
    """ This is a rectangle, it has a height and a width"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """ This is an instantiation with optional values """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        for a in range(self.__height - 1):
            print('#'*self.__width)
        return ('#'*self.__width)

    def __repr__(self):
        return "Rectangle(2, 4)"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
