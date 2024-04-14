#!/usr/bin/python3
""" First Rectangle """
from models.base import Base


class Rectangle(Base):
    """  inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class  constructor """
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)

        super().__init__()

        if id is not None:
            self.id = id
        else:
            self.id = self._Base__nb_objects

    def area(self):
        """ returns the area value of the Rectangle instance """
        return (self.__width * self.__height)

    def get_width(self):
        """ Returns the width """
        return self.__width

    def set_width(self, width):
        """ Sets the width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    def get_height(self):
        """ Returns the height """
        return self.__height

    def set_height(self, height):
        """ Sets the height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def get_x(self):
        """ Returns the x """
        return self.__x

    def set_x(self, x):
        """ Sets the x """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def get_y(self):
        """ Returns the y """
        return self.__y

    def set_y(self, y):
        """ Sets the y """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ getter for width """
        self.set_width(value)

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ getter for heigt """
        self.set_height(value)

    @property
    def x(self):
        """ getter for width """
        return self.__x

    @x.setter
    def x(self, value):
        self.set_x(value)

    @property
    def y(self):
        """ getter for width """
        return self.__y

    @y.setter
    def y(self, value):
        self.set_y(value)

    def display(self):
        """ displays the rectangle using '#' """
        a = 0
        while a < self.__height:
            b = 0
            while b < self.__width:
                print("#", end="")
                b += 1
            print()
            a += 1
