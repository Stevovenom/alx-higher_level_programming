#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_duplicates(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        """Test with a list containing floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_mixed_types(self):
        """Test with a list containing mixed types (ints and floats)"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        self.assertEqual(max_integer([-1, -2.5, -3]), -1)

if __name__ == '__main__':
    unittest.main()

