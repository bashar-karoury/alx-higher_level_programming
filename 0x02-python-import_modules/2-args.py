#!/usr/bin/python3
import sys
argv_len = len(sys.argv)
if __name__ == "__main__":
    if argv_len == 1:
        print("{} arguments.".format(argv_len - 1))
    else:
        print("{} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print("{}: {}".format(i, sys.argv[i]))
