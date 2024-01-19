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
