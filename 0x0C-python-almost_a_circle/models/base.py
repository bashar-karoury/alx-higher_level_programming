#!/usr/bin/python3
""" Module of Base class
"""


class Base:
    """ Base class for all other classes
        to manage id attribute of sub classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method for objects of this class

           Args:
                id (int) : id of object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
