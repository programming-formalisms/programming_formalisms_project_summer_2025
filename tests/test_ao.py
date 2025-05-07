"""Tests for src.learners.utils_ao"""

import unittest

from src.learners.utils_ao import is_roman_numeral

class TestUtilsAO(unittest.TestCase):

    """Class to test the code in src.learners.utils_ao."""

    # Test if it is a roman numeral
    def test_roman_numeral(self):
        """The input is a roman numeral"""
        self.assertTrue('I')
        self.assertTrue('II')
        self.assertTrue('V')
        self.assertTrue('X')
        self.assertTrue('L')
        self.assertFalse('A')
        