#!/usr/bin/python3
""" Module that contains add_attribute
"""


def add_attribute(obj, name, value):
    """ function that adds new attribute to object if it is
        possible

        Args:
            obj (object): any object
            name : name of attribute
            value: value of attribute to be added
    """

    if (
        type(obj).__module__ == 'builtins' or
        hasattr(obj, name) or
        (
            hasattr(obj, '__slots__') and
            name not in getattr(obj, '__slots__', [])
        )
    ):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
