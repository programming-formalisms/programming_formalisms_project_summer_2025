
def is_even(value):
    """Checks if the value is even"""
    if not isinstance(value, (int, float)):
        raise TypeError("Non-numeric value given")
    if abs(int(value) - value) > 0:
        raise ValueError("Non-integer value given")
    return value % 2 == 0

# Tests for is_even
assert is_even.__doc__

assert is_even(4)
assert not is_even(3)

try:
    is_even(3.5) # "not well defined for non-integer numbers"
    is_even("2")
except ValueError:
    assert True
else:
    assert False

try:
    is_even("2")
except TypeError:
    assert True
else:
    assert False