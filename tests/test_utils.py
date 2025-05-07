"""Tests all code in src.weather.utils."""
import unittest

from src.weather.utils import celsius2kelvin


class TestUtils(unittest.TestCase):

    """Class to test the code in src.weather.utils."""

    def test_celsius2kelvin_documentation(self):
        """Docstring exists"""
        self.assertTrue(celsius2kelvin.__doc__)
    
    def test_celsius2kelvin_calculations(self):
        """Calculations are correct"""
        self.assertEqual(celsius2kelvin(-273), 0)
    
    def test_celsius2kelvin_input(self):
        """The input is correct"""
        self.assertRaises(TypeError, celsius2kelvin, "string")
   
