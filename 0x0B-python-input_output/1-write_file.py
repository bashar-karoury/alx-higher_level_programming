#!/usr/bin/python3
""" This Module contains write_file function
"""


def write_file(filename="", text=""):
    """ function that writes a text to specified file
        to stdout

        Args:
            filename (str): string of file name
            text (str): text to be written
    """

    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
