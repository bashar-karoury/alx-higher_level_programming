#!/usr/bin/python3
""" This module contains matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """ This function multiply two matrices

        Args:
            m_a (list of lists): fisrt matrix
            m_b (list of lists): secons matrix
        Returs:
            (float): result of multiplication
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if not m_a:
        raise ValueError("m_a can't be empty")

    if not m_b:
        raise ValueError("m_a can't be empty")
    if type(m_a[0]) == list:
        a_row_size = len(m_a[0])
    if type(m_b[0]) == list:
        b_row_size = len(m_b[0])

    for lst in m_a:
        if type(lst) != list:
            raise TypeError("m_a must be a list of lists")
        if not lst:
            raise ValueError("m_a can't be empty")
        if len(lst) != a_row_size:
            raise TypeError("each row of m_a must be of the same size")
        for element in lst:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for lst in m_b:
        if type(lst) != list:
            raise TypeError("m_b must be a list of lists")
        if not lst:
            raise ValueError("m_b can't be empty")
        if len(lst) != b_row_size:
            raise TypeError("each row of m_b must be of the same size")
        for element in lst:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if a_row_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    transposed = [list(column) for column in zip(*m_b)]

    i = 0
    j = 0
    result = [[] for _ in range(len(m_a))]
    for row_a in m_a:
        for row_b in transposed:
            result[i].append(sum([x * y for x, y in zip(row_a, row_b)]))
        i += 1
    return result
