"""Tests all code in src.learners.richel."""
import unittest

from learners.viktor.get_digits import get_digits


class TestGetDigits(unittest.TestCase):

    """Class to test the code in src.learners.richel."""

    def test_get_digits(self):
        """The function 'get_name' returns the correct name."""
        self.assertEqual(get_digits(123),[1,2,3])
