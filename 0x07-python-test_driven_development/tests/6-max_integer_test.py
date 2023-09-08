"""Unittest for function that returns the maximum number in a list"""

import unittest
#Import module
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_integers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_integers(self):
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        result = max_integer([1, -2, 5, -4])
        self.assertEqual(result, 5)

    def test_single_element(self):
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_all_same_elements(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
