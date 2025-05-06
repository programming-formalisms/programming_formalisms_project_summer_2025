def is_odd(x):
    """Determine if a number is odd."""
    return x % 2 != 0

assert is_odd.__doc__
assert is_odd(2) == False
assert is_odd(3) == True