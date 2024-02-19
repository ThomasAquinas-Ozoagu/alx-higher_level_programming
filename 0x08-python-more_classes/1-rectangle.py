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
    def width(self, widt):
        """ This method modifies the private attribute"""
        if type(widt) != int:
            raise TypeError("width must be an integer")
        if widt < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = widt


    @height.setter
    def height(self, heigh):
        """ This method modifies the private attribute"""
        if type(heigh) != int:
            raise TypeError("height must be an integer")
        if heigh < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = heigh
