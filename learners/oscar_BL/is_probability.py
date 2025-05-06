
def is_probability(value):
    """Checks if the value is between 0 and 1 (is probability)"""
    assert isinstance(value, (float, int))
    return 0 <= value <= 1


assert is_probability.__doc__

assert is_probability(0.4)
assert is_probability(0)
assert is_probability(1)
assert not is_probability(1.5)
assert not is_probability(2)
assert not is_probability(-1)

try:
    is_probability("0.5")
except AssertionError:
    assert True
else:
    assert False