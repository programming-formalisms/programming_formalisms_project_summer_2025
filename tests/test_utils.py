"""Tests all code in src.learners.utils."""
import unittest

from src.weather.utils import celsius2kelvin


class TestUtils(unittest.TestCase):

    """Class to test the code in src.weather.utils."""

    def test_celsius2kelvin_documentation(self):
        """Docstring exists"""
        self.assertTrue(celsius2kelvin.__doc__)
    
    def test_celsius2kelvin_calculations(self):
        """Correctness of the calculations"""
        self.assertEqual(celsius2kelvin(-273), 0)
    
    #def test_celsius2kelvin_input(self):
    #    """Chekcs the input correctness"""
    #    self.assertRaises(TypeError, celsius2kelvin, "string")

    
