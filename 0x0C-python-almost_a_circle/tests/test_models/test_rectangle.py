#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Test cases for the Rectangle module"""


class TestRectangle(unittest.TestCase):
    """class to test for rectangle"""
    def setUp(self):
        """initializing the constructor"""
        self.rect = Rectangle(5, 3, 1, 2, 7)

    def tearDown(self):
        """deleting created constructor"""
        del self.rect

    def test_width(self):
        """testing the width getter"""
        self.assertEqual(self.rect.width, 5)

    def test_height(self):
        """testing the height getter"""
        self.assertEqual(self.rect.height, 3)

    def test_x(self):
        """testing the x-coordinate getter"""
        self.assertEqual(self.rect.x, 1)

    def test_y(self):
        """testing the y-coordinate getter"""
        self.assertEqual(self.rect.y, 2)

    def test_id(self):
        """testing the id for the rectangle"""
        self.assertEqual(self.rect.id, 7)

    def test_width_string(self):
        """testing width with a string instead of an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle("String", 5)

    def test_width_bool(self):
        """testing width with a boolean value instead of an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 5)

    def test_height_string(self):
        """testing height with a string instead of an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle("String", 3)

    def test_height_bool(self):
        """testing height with a boolean instead of an integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 3)



if __name__ == "__main__":
    unittest.main()
