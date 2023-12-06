#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for i in range(0, 3):
        sq_matrix.append(list(map(lambda x: x**2, matrix[i])))
    return sq_matrix
