#!/usr/bin/python3
import sys
if __name__ == "__main__":
    SUM = 0
    for arg in sys.argv[1:]:
        SUM += int(arg)
    print("{}".format(SUM))
