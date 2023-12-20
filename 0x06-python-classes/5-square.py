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

    def my_print(self):
        """prints square shape of object
        """
        if self.__size != 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('#', end='')
                print(end='\n')
        else:
            print(end='\n')
