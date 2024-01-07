#!/usr/bin/python3
""" This Module contains print_square function """


def print_square(size):
    """ prints square

    Args:
        size (int): size of square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print("")
