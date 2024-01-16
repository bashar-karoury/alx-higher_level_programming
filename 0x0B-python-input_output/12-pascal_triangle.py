#!/usr/bin/python3
""" Module that contains pascale_triangle function
"""


def pascal_triangle(n):
    """ function that returns a list of lists of integers representing
        pascal's triangle

        Args:
            n (int): number of rows

        Returns:
            (list of lists): each list contins row
    """

    if n <= 0:
        return []
    else:
        lst = [[] for i in range(n)]
        lst[0].append(1)
        if n == 1:
            return lst
        lst[1].append(1)
        lst[1].append(1)
        if n == 2:
            return lst
        for i in range(2, n):
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    lst[i].append(1)
                else:
                    lst[i].append(lst[i-1][j-1] + lst[i-1][j])
        return lst
