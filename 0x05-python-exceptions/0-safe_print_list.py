#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    for element in my_list:
        try:
            if i < x:
                print(element, end='')
                i = i + 1
        except Exception as exp:
            print(exp)
    print(end='\n')
    return i
