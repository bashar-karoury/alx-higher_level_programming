#!/usr/bin/python3
"""This module provides class Rectangle."""


class Rectangle:
    """A Rectangle class."""
    def __init__(self, width=0, height=0):
        """ Initialize new object of class

        Args:
            width (int): width of rec
            height (int): height of rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width of rec."""
        return self.__width

    @property
    def height(self):
        """ get height of rec."""
        return self-__height

    @width.setter
    def width(self, value):
        """ set width of rec

        Args:
            value (int): width of rec
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height of rec

        Args:
            value (int): height of rec
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
