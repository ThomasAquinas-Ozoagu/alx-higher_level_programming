#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Square:
    """ This is an empty class, the methods/attributes will come later"""
    def __init__(self, size=0):
        """ This initializes the attributes of the class"""
        self.size = size

    @property
    def size(self):
        """ This method returns the value of the private attribute"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """ This method modifies the private attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                print("{}".format("#"*self.__size))
