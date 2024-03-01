#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Rectangle:
    """ This is a rectangle, it has a height and a width"""
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """ This is an instantiation with optional values """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1


    """def print_symbol(self, symbol):
        self.print_symbol = str(symbol) """

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
        """ This returns the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ This returns the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ This expresses the rectangle in 2D """
        if self.__height == 0 or self.__width == 0:
            return ""
        for a in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        return (str(self.print_symbol) * self.__width)

    def __repr__(self):
        """ This shows how the class can be used """
        return "Rectangle(2, 4)"

    def __del__(self):
        """ This destroys an instance of the class """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ This compares two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ This redefines the rectangle as a square """
        return cls(size, size)
