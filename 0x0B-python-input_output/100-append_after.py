#!/usr/bin/python3
""" Module of function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+', encoding="utf-8") as f:
        old_txt = ""
        for line in f:
            old_txt += line
            if search_string in line:
                old_txt += new_string
        f.seek(0)
        f.write(old_txt)
