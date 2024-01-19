#!/usr/bin/python3
""" Module of rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherited from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function for this class

            Args:
                width (int): width of rec
                height (int): height of rec
                x (int): x coordination
                y (int): y coordintation
                id (int): id of object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter function

            Returns:
                (int) : width of rec
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter function

            Args:
                width (int): width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter function

            Returns:
                (int) : height of rec
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter function

            Args:
                height (int): height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter function

            Returns:
                (int) : x of rec
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter function

            Args:
                x (int): x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """ getter function

            Returns:
                (int) : y of rec
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter function

            Args:
                y (int): y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
