"""Tests all code in src.learners.is_number."""
import unittest

from src.learners.is_number import is_number

class TestUtils(unittest.TestCase):

    """Class to test the code in src.learners.ida_utils."""

    def test_is_number_has_documentation(self):
        """The function 'is_number' has documentation."""
        self.assertTrue(is_number.__doc__)
        self.assertIsNotNone(is_number.__doc__)

    def test_is_number_is_number(self):
        """The function 'is_number' can check if the input is a number"""
        self.assertTrue(is_number(5))
        self.assertFalse(is_number("hello"))