#!/usr/bin/python3
""" First Rectangle """
from models.base import Base


class Rectangle(Base):
    """  inherits from Base """
#    self.__nb_objects = super.__nb_objects
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class  constructor """
        self.__width = width
        self.__height = height
        __x = x
        __y = y
        super().__init__()
        if id is not None:
            self.id = id
        else:
            self.id = self._Base__nb_objects

    def get_width(self):
        """ Returns the width """
        return self.__width

    def set_width(self, value):
        """ Sets the width """
        self.__width = value

    def get_height(self):
        """ Returns the height """
        return self.__height

    def set_height(self, value):
        """ Sets the height """
        self.__height = value

    def get_x(self):
        """ Returns the x """
        return self.__x

    def set_x(self, value):
        """ Sets the x """
        self.__x = value

    def get_y(self):
        """ Returns the y """
        return self.__y

    def set_y(self, value):
        """ Sets the y """
        self.__y = value
