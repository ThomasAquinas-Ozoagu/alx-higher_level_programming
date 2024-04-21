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

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.set_width(value)
        self.set_height(value)

    def update(self, *args, **kwargs):
        """ updates square with both keyworded and non keyworded arguments """
        if args and args != []:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.set_x(args[2])
            if len(args) > 3:
                self.set_y(args[3])

        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.set_x(kwargs['x'])
            if 'y' in kwargs:
                self.set_y(kwargs['y'])
