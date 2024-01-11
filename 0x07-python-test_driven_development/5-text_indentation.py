#!/usr/bin/python3
""" This module contains text_indentation() function """


def text_indentation(text):
    """ This functions indent given text and prints 2 new
        lines after each of ., ?, :

        Args:
            text (str): text to be indented
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    next_is_new_line = True
    for c in text:
        if next_is_new_line and c == ' ':
            pass
        else:
            print(c, end='')
            next_is_new_line = False
        if c in ['.', '?', ':']:
            print("\n")
            next_is_new_line = True
