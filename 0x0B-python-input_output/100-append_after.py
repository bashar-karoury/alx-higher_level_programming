#!/usr/bin/python3
""" Module of function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ function that append a line of string after each line
        containing specific line string

        Args:
            filename (str): filename to read from and edit
            search_string(str): string to search for in lines
            new_string(str): string line to append after found lines
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        old_txt = ""
        for line in f:
            old_txt += line
            if search_string in line:
                old_txt += new_string
        f.seek(0)
        f.write(old_txt)
