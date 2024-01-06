#!/usr/bin/python3
"""This module provides class Rectangle."""


class Rectangle:
    """A Rectangle class."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize new object of class

        Args:
            width (int): width of rec
            height (int): height of rec
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ get width of rec."""
        return self.__width

    @property
    def height(self):
        """ get height of rec."""
        return self.__height

    @width.setter
    def width(self, value):
        """ set width of rec

        Args:
            value (int): width of rec
        """
        if not type(value) is int:
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
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate area of rec

        Returns:
            int: area of rec
        """
        return self.height * self.width

    def perimeter(self):
        """ calculate perimeter of rec

        Returns:
            int: perimeter of rec
        """
        if self.height and self.width:
            return 2 * self.height + 2 * self.width
        else:
            return 0

    def __str__(self):
        """ draw rec."""
        string = ""
        if self.height and self.width:
            for i in range(self.height):
                j = 0
                for j in range(self.width):
                    string += str(self.print_symbol)
                if i < self.height - 1:
                    string += '\n'
        return string

    def __repr__(self):
        """ give representation of rec"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """ deini"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rec based on area

        Args:
            rect_1 (Rectangle): first rec
            rect_2 (Rectangle): second rec

        Returns:
            Rectangle: the biggest one based on are
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new rec instance with width = height = size

        Args:
            size (int): size of square

        Returns:
            Rectangle: new instance of Rectrangle
        """
        return Rectangle(size, size)
