def is_odd(x):
    """Determine if a number is odd."""
    if not isinstance(x, int):
        raise TypeError("Input must be an integer")
    return x % 2 != 0

assert is_odd.__doc__
assert is_odd(2) == False
assert is_odd(3) == True
try:
    is_odd('x')
except TypeError:
    print("TypeError raised in test 4")

assert is_odd(2.0) == False