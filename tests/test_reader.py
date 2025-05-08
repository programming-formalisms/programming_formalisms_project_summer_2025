"""Tests all code in src.weather.reader."""
import unittest

from src.weather.reader import read_data


class TestReader(unittest.TestCase):

    """Class to test the code in src.weather.reader."""

    def test_reader_has_documentation(self):
        """The function 'is_zero' has documentation."""
        self.assertTrue(read_data.__doc__)

    def test_reader_reads_file(self):
        self.assertRaises(RuntimeError, read_data, "wrong_filepath")
    
    def test_reader_returns_list(self):
        #self.assertTrue(isinstance(read_data("/Users/xiuqi.ji/Library/CloudStorage/OneDrive-KarolinskaInstitutet/NAISS/Programming_Formalisms/programming_formalisms_project_summer_2025/data/uppsala_tm_1722-2022.dat"),list))
        self.assertTrue(isinstance(read_data("/programming_formalisms_project_summer_2025/data/uppsala_tm_1722-2022.dat"),list))