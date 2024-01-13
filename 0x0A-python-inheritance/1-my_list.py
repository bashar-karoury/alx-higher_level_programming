#!/usr/bin/python3
""" Module that contains MyList class
"""


class MyList(list):
    """ subclass of list
    """
    def print_sorted(self):
        """ print sorted list
        """
        print(sorted(self))
