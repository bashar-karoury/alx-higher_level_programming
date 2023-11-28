#!/usr/bin/python3
for c in range(97, 123):
    if c == ord('q') or c == ord('e'):
        continue
    print("{0:c}".format(c), end='')
