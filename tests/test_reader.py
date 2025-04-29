"""Tests all code in src.weather.reader."""
import unittest

from src.weather.reader import read_data


class TestReader(unittest.TestCase):

    """Class to test the code in src.weather.reader."""

    def test_read_data(self):
        """The function 'read_data' exists."""
        read_data()
