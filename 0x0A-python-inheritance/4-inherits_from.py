#!/usr/bin/python3
""" Module contains inherits_from function
"""


def inherits_from(obj, a_class):
    """ Function that check if object kind of specified class
    """
    if obj.__class__ == a_class:
        return False
    else:
        return issubclass(obj.__class__, a_class)
