#!/usr/bin/python3
""" Module that contains Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherited from BaseGeometry
    """

    def __init__(self, width, height):
        """ initialization method

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ function that returns the area of rec object

            Returns:
                int: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """string format of object when printed

            Returns:
                str: string representation of rec
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
