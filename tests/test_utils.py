"""Tests all code in src.learners.utils."""
import unittest

from src.weather.utils import celsius2kelvin


class TestUtils(unittest.TestCase):

    """Class to test the code in src.weather.utils."""

    def test_celsius2kelvin(self):
        """The function 'celsius2kelvin' returns the correct temperature."""
        self.assertEqual(celsius2kelvin(-273), 0)
