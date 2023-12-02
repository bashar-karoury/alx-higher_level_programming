#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    div_list = [x % 2 == 0 for x in my_list]
    return div_list
