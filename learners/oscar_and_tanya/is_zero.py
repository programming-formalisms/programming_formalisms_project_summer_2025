
def is_zero(value):
    """ Checks if the value is zero """
    if not isinstance(value, (float,int)):
        raise TypeError("Value is not of numeric type")
    return value == 0

""" Defined 'tests' for the function 'is_zero' """
assert is_zero.__doc__

assert is_zero(0) == True
assert is_zero(1) == False

try:
    is_zero("0")
except TypeError:
    assert True
else:
    assert False, "No exception raised for string input"