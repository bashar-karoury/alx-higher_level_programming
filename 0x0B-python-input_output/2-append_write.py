#!/usr/bin/python3
""" This Module contains append_write function
"""


def append_write(filename="", text=""):
    """ function that append writes a text to specified file
        to stdout

        Args:
            filename (str): string of file name
            text (str): text to be written
    """

    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
