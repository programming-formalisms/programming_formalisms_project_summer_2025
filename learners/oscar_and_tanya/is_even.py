
def is_even(value):
    """Checks if the value is even"""
    return value % 2 == 0

# Tests for is_even
assert is_even.__doc__

assert is_even(4)
assert not is_even(3)

assert is_even(3.5), "not well defined for non-integer numbers"