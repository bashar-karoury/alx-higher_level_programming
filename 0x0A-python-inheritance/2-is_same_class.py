#!/usr/bin/python3
""" Module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """ Function that check if object from specified class
    """
    return type(obj) == a_class
