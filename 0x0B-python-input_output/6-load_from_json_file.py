#!/usr/bin/python3
""" This Module contains load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object form a JSON file

        Args:
            filename (str): string of file name
    """

    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
