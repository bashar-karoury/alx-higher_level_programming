#!/usr/bin/python3


def multiple_returns(sentence):
    tuple_sen = ()
    tuple_sen = tuple_sen + (len(sentence),)
    if len(sentence) > 0:
        tuple_sen = tuple_sen + (sentence[0],)
    else:
        tuple_sen = tuple_sen + (None,)

    return tuple_sen
