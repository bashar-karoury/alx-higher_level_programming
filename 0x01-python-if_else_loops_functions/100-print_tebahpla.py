#!/usr/bin/python3

for c in range(122, 96, -1):
    if c % 2 != 0:
        c = c - 0x20	
    print("{0:c}".format(c), end='')
