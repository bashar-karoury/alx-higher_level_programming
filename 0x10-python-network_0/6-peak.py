#!/usr/bin/python3
""" This module contains function to find peak of list of integers
"""


def find_peak(l):
    """ find peak of list of integeres
    """
    if not l:
        return None
    if len(l) == 1:
        return l

    possible_peak = l[0]
    check_next = 0
    for i in range(1, len(l)):
        if l[i] >= l[i-1]:
            possible_peak = l[i]
            check_next = 1
        else:
            if check_next:
                break
    return (possible_peak)
