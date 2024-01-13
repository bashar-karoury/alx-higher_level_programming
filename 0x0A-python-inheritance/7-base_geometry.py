#!/usr/bin/python3
""" This module contains incomplete implementation
"""


class BaseGeometry:
    """ Class of BaseGeometry
    """

    def area(self):
        """ unfinished implementation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validation method

            Args:
                name (str): name
                value (int): value
            Returns:
                Nothing if value is greater than zero,
                raise exception otherwise
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
