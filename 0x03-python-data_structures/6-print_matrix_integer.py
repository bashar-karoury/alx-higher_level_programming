#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        first = True
        for j in i:
            if first is False:
                print(" ", end='')
            print("{}".format(j), end='')
            first = False
        print("")
