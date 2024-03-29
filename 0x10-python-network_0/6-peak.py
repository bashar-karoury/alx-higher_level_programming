#!/usr/bin/python3
""" This module contains function to find peak of list of integers
"""


def find_peak(l):
    """ find peak of list of integeres
    """
    if not l:
        return None

    if len(l) == 1:
        return (l[0])
    # get the middle value
    middle = int(len(l)/2)

    # check middle if a find_peak
    if middle > 0 and l[middle] <= l[middle - 1]:
        # go left
        return find_peak(l[:middle])
    elif middle < len(l) - 1 and l[middle] <= l[middle + 1]:
        # go right
        return find_peak(l[middle+1:])
    else:
        return l[middle]
