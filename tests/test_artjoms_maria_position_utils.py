import unittest

from src.learners.artjoms_maria_position import Position

class TestPosition(unittest.TestCase):
    def test_input_type(self):
        self.assertRaises(TypeError, Position(), ("string", 0))
