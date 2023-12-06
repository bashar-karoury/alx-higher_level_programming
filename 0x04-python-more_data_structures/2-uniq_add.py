#!/usr/bin/python3
def uniq_add(my_list=[]):
    SUM = 0
    for i in set(my_list):
        SUM += i
    return SUM
