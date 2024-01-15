#!/usr/bin/python3
""" This Module contains save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an object to specified file

        Args:
            my_obj (object): object to be serilaized
            filename (str): string of file name
    """

    with open(filename, mode='w', encoding='utf-8') as a_file:
        return json.dump(my_obj, a_file)
