#!/usr/bin/python3
import unittest
from models.base import Base


"""Test cases for base module"""


class TestBase(unittest.TestCase):
    """class to test base"""
    def test_id_valid(self):
        """test for a valid id"""
        valid_id = Base(42)
        self.assertEqual(valid_id.id, 42)

    def test_id_negative(self):
        """test for a negative id"""
        negative_num = Base(-10)
        self.assertEqual(negative_num.id, -10)

    def test_id_string(self):
        """test for an id that's a string"""
        char_str = Base("Unittesting")
        self.assertEqual(char_str.id, "Unittesting")
