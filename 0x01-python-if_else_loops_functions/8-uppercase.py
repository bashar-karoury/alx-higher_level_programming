#!/usr/bin/python3


def uppercase(str):
    for c in str:
        if ord(c) > 96:
            print("{0:c}".format(ord(c) - 0x20), end='')
        else:
            print(c, end='')
    print()
