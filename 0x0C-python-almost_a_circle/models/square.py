#!/usr/bin/python3
""" Module of rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inherited from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init method

            Args:
                size (int): size of square
                x (int): x coordination
                y (int): y coordination
                id (int): id of object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square class
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ getter function

            Returns:
                (int) : size of seq
        """
        return self.width

    @size.setter
    def size(self, size):
        """ setter function

            Args:
                size (int): size
        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update attributes of square object
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ function to get dictionary representation of square
        """
        dct = {}
        dct['id'] = self.id
        dct['size'] = self.size
        dct['x'] = self.x
        dct['y'] = self.y
        return dct
