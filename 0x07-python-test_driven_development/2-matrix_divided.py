#!/usr/bin/python3
""" This is Module that contains matrix_divided function"""


def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    row_1_size = len(matrix[0])
    new_matrix = []
    for l in matrix:
        if type(l) != list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(l) != row_1_size:
            raise TypeError("Each row of the matrix"
                            " must have the same size")
        new_list = []
        for i in l:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
