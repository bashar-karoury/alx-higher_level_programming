#!/usr/bin/python3


def add_integer(a, b=98):
    """ Add integers
    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: Sum of two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
