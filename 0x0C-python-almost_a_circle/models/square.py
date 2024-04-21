#!/usr/bin/python3
""" And now, the Square! """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class  constructor """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """ The string representation for the class """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                           self.x, self.y, self.width)
