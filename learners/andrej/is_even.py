def is_even(x):
    """determines if the input number is even or not"""
    if not isinstance(x, (float, int)):
        raise TypeError("The input is not numeric.")
    return x % 2 == 0

assert is_even.__doc__
assert is_even(2) == True
assert is_even(3) == False

exception_raised = False

try:
    is_even("string")
except:
    exception_raised = True

assert exception_raised
