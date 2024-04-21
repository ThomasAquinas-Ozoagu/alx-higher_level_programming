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

        super().__init__(id)

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
        z = 0
        while z < self.__y:
            print()
            z += 1
        a = 0
        while a < self.__height:
            b = 0
            print(" " * self.__x, end="")
            while b < self.__width:
                print("#", end="")
                b += 1
            print()
            a += 1

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.__x, self.__y,
                                                 self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args and args != []:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.set_width(args[1])
            if len(args) > 2:
                self.set_height(args[2])
            if len(args) > 3:
                self.set_x(args[3])
            if len(args) > 4:
                self.set_y(args[4])

        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.set_width(kwargs['width'])
            if 'height' in kwargs:
                self.set_height(kwargs['height'])
            if 'x' in kwargs:
                self.set_x(kwargs['x'])
            if 'y' in kwargs:
                self.set_y(kwargs['y'])
