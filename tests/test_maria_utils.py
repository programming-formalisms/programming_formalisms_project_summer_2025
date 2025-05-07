"""Tests all code in src.learners.maria_utils."""
import unittest

from src.learners.maria_utils import is_zero, is_prime

class TestMariaUtils(unittest.TestCase):

    """Class to test the code in src.learners.maria_utils."""

    def test_is_zero_has_documentation(self):
         """The function 'is_zero' has documentation."""
         self.assertTrue(is_zero.__doc__)
         self.assertIsNotNone(is_zero.__doc__)

    def test_is_zero_responds_correctly_to_ints(self):
         """The function 'is_zero' responds correctly to integers."""
         self.assertTrue(is_zero(0))
         self.assertFalse(is_zero(1))

    def test_is_zero_raises_an_exception_upon_non_ints(self):
         """The function 'is_zero' raises an exception upon non-ints."""
         self.assertRaises(TypeError, is_zero, {1, 2})
         self.assertRaises(TypeError, is_zero, "I am a string")

    def test_is_prime(self):
        """The function 'is_zero' responds correctly to integers."""
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(6))