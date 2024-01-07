#!/usr/bin/python3
""" This module contains function of say_my_name"""


def say_my_name(first_name, last_name=""):
    """ This function prints name passed as args

    Args:
        first_name: (string) first name
        last_name: (sring) last name
    """
    if type(first_name) != str or len(first_name) == 0:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
