#!/usr/bin/python3
""" Module contains MyInt
"""


class MyInt(int):
    """ class MyInt with reversed == and != operator
    """

    def __eq__(self, other):
        """ == operator overriding function with reversed
            functionality

            Args:
                other (MyInt): other object of same class

            Returns:
                (bool): True if two are not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ != operator overriding function with reversed
            functionality

            Args:
                other (MyInt): other object of same class

            Returns:
                (bool): True if two are not equal, False otherwise
        """
        return super().__eq__(other)
