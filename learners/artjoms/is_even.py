def is_even(x):
    """Determines if the input number is even or not"""
    if not isinstance(x, (float, int)):
        raise TypeError("The input is not numeric.")

    return x % 2 == 0

def is_odd(x):
    """Determines if the input number is odd"""
    return not is_even(x)

assert is_even.__doc__
assert is_even(2) == True
assert is_even(3) == False

exception_raised = False

try:
    is_even("string")
except:
    exception_raised = True

assert exception_raised

assert is_odd(3) == True
assert not is_odd(2)
assert is_odd.__doc__
try:
    is_odd("string")
except TypeError:
    exception = True
assert exception
assert is_odd(2.2)