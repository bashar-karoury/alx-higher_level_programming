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

    @property
    def size(self):
        """getter of size attribute
        Returns:
            int: size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size attribute.

        Args:
        value (int): size of square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Get area of square instance
        Returns:
            int: area of square
        """
        return ((self.__size)**2)

    def __eq__(self, other):
        """Check Equality of two squares
        Args:
            other (square): the other object to compare to
        Returns:
            bool: True if equal or False
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check Non Equality of two squares
        Args:
            other (square): the other object to compare to
        Returns:
            bool: True if not equal or False
        """
        return self.area() != other.area()

    def __le__(self, other):
        """Check is less of two squares
        Args:
            other (square): the other object to compare to
        Returns:
            bool: True if less or False
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """Check is greater of two squares
        Args:
            other (square): the other object to compare to
        Returns:
            bool: True if greater or False
        """
        return self.area() > other.area()

    def __le__(self, other):
        """Check less or equal of two squares
        Args:
            other (square): the other object to compare to
        Returns:
            bool: True if less than or equal or False
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """Check great of equal of two squares
        Args:
            other (square): the other object to compare to
        Returns:
            bool: True if great or equal or False
        """
        return self.area() >= other.area()
