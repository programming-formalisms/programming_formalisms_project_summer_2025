"""Tests for src.learners.utils_ao"""

import unittest

from src.learners.utils_ao import is_roman_numeral

class TestUtilsAO(unittest.TestCase):

    """Class to test the code in src.learners.utils_ao."""

    # Test if it is a roman numeral
    def test_roman_numeral(self):
        """The input is a roman numeral"""
        self.assertTrue(is_roman_numeral('I'))
        self.assertTrue(is_roman_numeral('II'))
        self.assertTrue(is_roman_numeral('V'))
        self.assertTrue(is_roman_numeral('X'))
        self.assertTrue(is_roman_numeral('L'))
        self.assertFalse(is_roman_numeral('A'))
        