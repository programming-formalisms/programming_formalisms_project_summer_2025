"""Tests all code in src.learners.utils."""
import unittest

from src.learners.utils import get_name


class TestUtils(unittest.TestCase):

    """Class to test the code in src.learners.utils."""

    def test_get_name(self):
        """The function 'get_name' returns the correct name."""
        self.assertEqual(get_name(), "utils")
