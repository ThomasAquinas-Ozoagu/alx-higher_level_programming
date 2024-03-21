#!/usr/bin/python3
""" Inheritance demonstration """


class BaseGeometry:
    """ This class will be used to practice how to display default
    class parameters'
    """
    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the variable VALUE, whose name is a STRING """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ This class will be used to practice inheritance """
    def __init__(self, width, height):
        """ Instantiation of Rectangle class
        BaseGeometry().__init__()
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Redefines the area method """
        return self.__width * self.__height

    def __str__(self):
        """ Invokes the str magic method """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Defines a shape different from Rectangle """
    def __init__(self, size):
        """ Initialize the class parameters """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Redefines the area method """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
