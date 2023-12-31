#!/usr/bin/python3
"""Module that provides Square

Classes:
    Square: simple square class
"""


class Square:
    """Square class
    Attributes:
        __size (int): size of square must be >= 0
        __position((int, int)): position of square
        ...
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the class.

        Args:
        size (int): size of square.
        position ((int, int)): position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of position attribute
        Returns:
            int: position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position attribute.

        Args:
        value (tuple): position of square.
        """
        v = value
        if not is_tuple_of_positive_2_int(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

            for n in range(self.position[1]):
                print(end='\n')
            for i in range(0, self.__size):
                for s in range(self.position[0]):
                    print(' ', end='')
                for j in range(0, self.__size):
                    print('#', end='')
                print(end='\n')
        else:
            print(end='\n')

    def __str__(self):
        """to be used by print
        """
        result = ""
        if self.__size != 0:
            for n in range(self.position[1]):
                result += '\n'
            for i in range(0, self.__size):
                for s in range(self.position[0]):
                    result += ' '
                for j in range(0, self.__size):
                    result += '#'
                if i != (self.__size - 1):
                    result += '\n'
        else:
            pass
        return result


def is_tuple_of_positive_2_int(value):
    """ test if the passed argument is tuple of two positive integers
    Args:
        value (tuple): tuple of int

    Returns:
        True if test passes, False else
    """
    result = True
    if type(value) != tuple:
        return False
    if len(value) != 2:
        return False
    if type(value[1]) != int or type(value[0]) != int:
        return False
    if value[0] < 0 or value[1] < 0:
        return False
    return True
