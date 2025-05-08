"""Tests all code in src.learners.andrej_artur_class."""
import unittest

from src.learners.andrej_artur_class import Parameters

class TestAndrejArturClass(unittest.TestCase):

    """Class to test the code in src.learners.andrej_artur_class."""

    # Test input parameters type for the class
    def test_param_types(self):
        """Test the bacteria number type"""
        self.assertRaises(TypeError, Parameters.__init__, "exp", 1000, "40", 50)

        # param0 = Parameters("exp", 1000, 49, 554)
        
        # param1 = Parameters(-20, -1000, "test", "test") # two wrong parameters
        # param2 = Parameters(20.245, 1000, "test", "test")

        
        # self.assertTrue(isinstance(param0.get_n_bacteria(), int))


       

        # self.assertTrue(TypeError, Parameters(20, 1000, "test", "test"))

        # self.assertRaises(TypeError, Parameters(20.245, 1000, "test", "test").get_n_bacteria, "n_bacteria parameter must be a int type")

        # self.assertRaises(TypeError, Parameters.get_n_bacteria, -20)
        # self.assertRaises(TypeError, Parameters.get_n_bacteria, "I am a string")

