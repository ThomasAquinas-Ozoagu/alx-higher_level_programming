#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Square:
    """ This is an empty class, the methods/attributes will come later"""
    def __init__(self, size=0, position=(0, 0)):
        """ This initializes the attributes of the class"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ This method returns the value of the private attribute"""
        return (self.__position)

    @position.setter
    def position(self, position):
        """ This method returns the value of the private attribute"""
        if type(position) != tuple or position[0]<0 or position[1]<0:
            raise TypeError("psition must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
               print("{}".format("\n"*(self.__position[1] - 1)))
            for a in range(self.__size):
                print("{}{}".format(" "*self.__position[0], "#"*self.__size))
