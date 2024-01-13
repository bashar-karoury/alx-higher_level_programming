#!/usr/bin/python3
""" This Module contains lookup function
"""


def lookup(obj):
    """ function that returns list of names in obj namespace
        Args:
            obj :(object) any object

        Return:
            (list): list of names associated with object
    """
    return dir(obj)
