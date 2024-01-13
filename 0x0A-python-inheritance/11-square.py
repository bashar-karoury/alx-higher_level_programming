#!/usr/bin/python3
""" Module that contains Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class
    """

    def __init__(self, size):
        """ Init function

            Args:
                size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ function to return area of square

            Returns:
                int: area of square
        """
        return self.__size ** 2

    def __str__(self):
        """ string representation of class objects
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
