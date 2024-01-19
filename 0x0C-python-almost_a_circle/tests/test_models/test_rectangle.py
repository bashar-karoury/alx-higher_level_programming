""" unit test of class Base
"""
import unittest
import sys
sys.path.append('/home/bashar/alx-higher_level_programming/0x0C-python-almost_a_circle/models') 
Rectangle = __import__('rectangle').Rectangle

class TestRecInit(unittest.TestCase):
    """ Class that contains test cases of init function
    """

    def test_init_no_id(self):
        """ test init function auto incrementing id
        """
        rec = Rectangle(1, 2, 3, 4)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 1)

    def test_init_given_id(self):
        """ test init function assign given id to object
        """
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec1.id, 5)
