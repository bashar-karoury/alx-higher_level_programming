#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    rev = my_list[::-1]
    for item in reversed(my_list):
        print("{:d}".format(item))
