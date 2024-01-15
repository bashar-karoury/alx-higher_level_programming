#!/usr/bin/python3
""" Module that contians function to_json_string
"""
import json


def to_json_string(my_obj):
    """ function that retruns the JSON representation of an object

        Args:
            my_obj (object): any object

        Returns:
            JSON representation of file
    """
    return json.dumps(my_obj)
