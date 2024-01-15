#!/usr/bin/python3
""" Module that contians function from_json_string
"""
import json


def from_json_string(my_str):
    """ function that retruns object from JSON representation of an object

        Args:
            my_str (str): string

        Returns:
            (object): object from JSON
    """
    return json.loads(my_str)
