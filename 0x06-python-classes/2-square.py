#!/usr/bin/python3
"""Module that provides Square

Classes:
    Square: simple square class
"""


class Square:
    """Square class
    Attributes:
        __size (int): size of square must be >= 0
        ...
    """
    def __init__(self, size=0):
        """Initializes a new instance of the class.

        Args:
        size (float): size of square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
