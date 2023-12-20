#!/usr/bin/python3
"""Module that provides MagicClass

Classes:
    MagicClass: defines a circle
"""
import math


class MagicClass:
    """Magic class
    Attributes:
        radius (int): radius of circle
    """
    def __init__(self, radius):
        """Initializes a new instance of the class.

        Args:
        radius (int): radius of circle
        """
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """ Calculate area of circle
        Return (int): result
        """
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """ Calculate circumference of circle

        Returns(int): result
        """
        return (math.pi * 2 * self.radius)
