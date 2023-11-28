#!/usr/bin/python3


def uppercase(str):
    for c in str:
        asc = ord(c)
        if asc > 96:
            asc = asc - 0x20
        print("{:c}".format(asc), end='')
    print()
