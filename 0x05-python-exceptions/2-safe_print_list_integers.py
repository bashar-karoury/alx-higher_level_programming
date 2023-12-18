#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(0, x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                n = n + 1
        except ValueError as exp:
            print(exp)
    print(end='\n')
    return n
