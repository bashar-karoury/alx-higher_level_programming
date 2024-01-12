#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Testing_max_integer(unittest.TestCase):
    """ Unit testing class subbed from unittest.TestCase
    """

    def test_empty_list(self):
        """ testing function takes empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_One_element_list(self):
        """ testing functin takes list with one argument
        """
        self.assertEqual(max_integer([1]), 1)

    def test_Neg_element_list(self):
        """ testing functin takes list with one neg argument
        """
        self.assertEqual(max_integer([-1]), -1)

    def test_Normal_list(self):
        """ testing functin takes normal list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_Reverse_list(self):
        """ testing functin takes reveresed ordered list
        """
        self.assertEqual(max_integer([14, 3, 4]), 14)

    def test_Max_Middle_list(self):
        """ testing functin takes reveresed ordered list
        """
        self.assertEqual(max_integer([2, 6, 14, 3, 4]), 14)
