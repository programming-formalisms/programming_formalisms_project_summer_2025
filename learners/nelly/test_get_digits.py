import unittest
from get_digits import get_digits


class TestGetDigits(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(get_digits(1), [1])

    def test_multiple_digits(self):
        self.assertEqual(get_digits(314), [3, 1, 4])

    def test_multiple_inputs(self):
        with self.assertRaises(TypeError) as context:
            get_digits(12, 34)
        self.assertEqual(str(context.exception), "Expected one input but got 2")

    def test_negative_input(self):
        with self.assertRaises(TypeError) as context:
            get_digits(-5)
        self.assertEqual(str(context.exception), "Please only provide a positive integer")

    def test_negative_input(self):
        with self.assertRaises(TypeError) as context:
            get_digits('test')
        self.assertEqual(str(context.exception), "Please only provide integer value")


if __name__ == '__main__':
    unittest.main()

