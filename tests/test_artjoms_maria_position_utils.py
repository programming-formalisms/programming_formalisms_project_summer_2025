import unittest

from src.learners.artjoms_maria_position import Position

class TestPosition(unittest.TestCase):
    
    def test_input_type(self):
        """A TypeError is raised for non-numeric input"""
        self.assertRaises(TypeError, Position, "string0", "string1")
        self.assertRaises(TypeError, Position, 0, "string1")
        self.assertRaises(TypeError, Position, "string1", 1)
