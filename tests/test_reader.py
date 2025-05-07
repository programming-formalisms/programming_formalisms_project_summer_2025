"""Tests all code in src.weather.reader."""
import unittest

from src.weather.reader import read_data


class TestReader(unittest.TestCase):

    """Class to test the code in src.weather.reader."""

    def test_read_data(self):
        """The function 'read_data' exists."""
        self.assertFalse(read_data(""))

    def test_reader_has_documentation(self):
        """The function 'is_zero' has documentation."""
        self.assertTrue(read_data.__doc__)

    def test_reader_reads_file(self):
        self.assertTrue(read_data("../data/uppsala_tm_1722-2022.dat"))
