#!/usr/bin/python3
""" Module of function class_to_json
"""


def class_to_json(obj):
    """ function that returns the dictionary description of data structure
        for JSON serialization of an object

        Args:
            obj (object): any object

        Returns:
            JSON serialization of an object
    """
    return obj.__dict__
