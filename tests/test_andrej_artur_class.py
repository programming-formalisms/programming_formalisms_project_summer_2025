"""Tests all code in src.learners.andrej_artur_class."""
import unittest

from src.learners.andrej_artur_class import Parameters

class TestAndrejArturClass(unittest.TestCase):

    """Class to test the code in src.learners.andrej_artur_class."""

    # Test input parameters type for the class
    def test_bacteria_is_non_neg(self):
        """Test that n_bacteria is a non-negative integer"""
        self.assertRaises(TypeError, Parameters.__init__, ("1", 1, "a", "b"))
        self.assertRaises(TypeError, Parameters.__init__, (-2, 1, "a", "b"))
        self.assertRaises(TypeError, Parameters.__init__, (1.0, 1, "a", "b"))

    def test_timestamps_in_non_neg(self):
        """Test that n_timestamps is a non-negative integer"""
        self.assertRaises(TypeError, Parameters.__init__, (1, "1", "a", "b"))
        self.assertRaises(TypeError, Parameters.__init__, (1, -1, "a", "b"))
        self.assertRaises(TypeError, Parameters.__init__, (1, 1.0, "a", "b"))


