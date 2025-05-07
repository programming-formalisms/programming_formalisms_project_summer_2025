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

from src.learners.utils_ao import roman_to_numeral

class TestRomanUtilsAO(unittest.TestCase):

    "Class to test roman conversion in src.learners.utils_ao"

    def test_roman_to_int(self):
        """ Checks a few conversion cases from roman numerals to int"""
        self.assertEqual(roman_to_numeral("I"), 1)
        self.assertEqual(roman_to_numeral("V"), 5)
        self.assertEqual(roman_to_numeral("X"), 10)
        self.assertEqual(roman_to_numeral("L"), 50)
        self.assertEqual(roman_to_numeral("IX"), 9)
        self.assertEqual(roman_to_numeral("XX"), 20)
        self.assertEqual(roman_to_numeral("LX"), 60)
        self.assertEqual(roman_to_numeral("IXL"), 59)
        self.assertEqual(roman_to_numeral("LXXX"), 80)
        self.assertEqual(roman_to_numeral("XLIV"), 44)