#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    for i in range(0, 2):
        if len(tuple_a) < i+1:
            a = 0
        else:
            a = tuple_a[i]
        if len(tuple_b) < i+1:
            b = 0
        else:
            b = tuple_b[i]
        tuple_c = tuple_c + (a + b, )
    return tuple_c
