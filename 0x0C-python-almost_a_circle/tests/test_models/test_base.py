""" unit test of class Base
"""
import unittest
import sys
sys.path.append('/home/bashar/alx-higher_level_programming/0x0C-python-almost_a_circle/models') 
Base = __import__('base').Base

class TestBaseInit(unittest.TestCase):
    """ Class that contains test cases of init function
    """

    def test_init_auto_id(self):
        """ test init function auto incrementing id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_init_given_id(self):
        """ test init function assign given id to object
        """
        b4 = Base(101)
        self.assertEqual(b4.id, 101)
