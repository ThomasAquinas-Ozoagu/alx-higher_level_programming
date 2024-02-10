#!/usr/bin/python3
""" My first step to understanding OOP, I'm going to have so much fun"""


class Square:
    """ This is an empty class, the methods/attributes will come later"""
    def __init__(self, size=0):
        """ This initializes the attributes of the class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
