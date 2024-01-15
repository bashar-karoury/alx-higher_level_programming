#!/usr/bin/python3
""" This Module contains read_file function
"""


def read_file(filename=""):
    """ function that reads a text file and prints it is output
        to stdout

        Args:
            filename (str): string of file name
    """

    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
