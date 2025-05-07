"""Test 'get_digits.py in learners.maria_ole"""
import unittest

from src.learners.maria_ole import get_digits

class TestRichel(unittest.TestCase):

    """Class to test the code in learners.maria_ole"""

    def test_get_digits(self):
        """The function 'get_digits' does what it is supposed to."""
        self.assertIsInstance(get_digits(123), list)
        self.assertTrue(get_digits(123)[0] == 1)
        self.assertTrue(len(get_digits(123)) == 3)
        self.assertRaises(TypeError,get_digits(-5))
        self.assertRaises(TypeError,get_digits('Hello'))
        self.assertRaises(TypeError,get_digits(0.4))


