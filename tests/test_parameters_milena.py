"""Tests all code in src.weather.reader."""
import unittest

from src.learners.parameters_class_exercise1 import Parameters


class TestParameters(unittest.TestCase):

    """Class to test the code in src.weather.reader."""

    def test_input(self):
        """The class Parameters has a documentation."""
        self.assertIsNotNone(Parameters.__doc__)
    
    def test_type(self):
        """The class should have the data type called 'Parameters'. """
        self.assertEqual(str(type(Parameters(42, 1000, 'uniform', 'uniform'))), "<class 'src.learners.parameters_class_exercise1.Parameters'>")