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

    def test_init_no_id_x_y(self):
        """ test init function auto incrementing id
        """
        rec = Rectangle(1, 2)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test_init_no_id_y(self):
        """ test init function auto incrementing id
        """
        rec = Rectangle(1, 2, 3)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)
 
    def test_init_given_id(self):
        """ test init function assign given id to object
        """
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec1.id, 5)

    def test_non_int_width_validation(self):
        """ test width not int
        """
        with self.assertRaises(TypeError):
            rec = Rectangle('1', 2, 4, 5, 6)

    def test_non_int_height_validation(self):
        """ test height not int
        """
        with self.assertRaises(TypeError):
            rec = Rectangle(1, '2', 4, 5, 6)

    def test_non_int_x_validation(self):
        """ test x not int
        """
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, '4', 5, 6)

    def test_non_int_y_validation(self):
        """ test y not int
        """
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 4, '5', 6)

    def test_zero_width_validation(self):
        """ test width zero
        """
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 2, 4, 5, 6)

    def test_zero_height_validation(self):
        """ test height zero
        """
        with self.assertRaises(ValueError):
            rec = Rectangle(1, 0, 4, 5, 6)

    def test_neg_width_validation(self):
        """ test width negative
        """
        with self.assertRaises(ValueError):
            rec = Rectangle(-1, 2, 4, 5, 6)

    def test_neg_height_validation(self):
        """ test height negative
        """
        with self.assertRaises(ValueError):
            rec = Rectangle(1, -2, 4, 5, 6)

    def test_neg_x_validation(self):
        """ test x negative
        """
        with self.assertRaises(ValueError):
            rec = Rectangle(1, 2, -4, 5, 6)

    def test_neg_y_validation(self):
        """ test y negative
        """
        with self.assertRaises(ValueError):
            rec = Rectangle(1, 2, 4, -5, 6)

    def test_area(self):
        rec = Rectangle(2, 4, 5, 6)
        self.assertEqual(rec.area(), 8)

    def test_display(self):
        rec = Rectangle(4, 6)

    def test_str(self):
        rec = Rectangle(1, 2, 3, 4, 5)
