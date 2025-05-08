# Exercise 1
def is_zero(x):
    "x is input, returns True if x is zero, False otherwise"
    return x == 0

assert is_zero.__doc__
assert is_zero(0) == True, "Expected True for input 0"
assert is_zero(0)
assert is_zero(1) == False, "Expected False for input 1"
assert not is_zero(1) == True

# Exercise 2

def is_even(x):
    '''Check if input is even'''
    result = x % 2
    if result == 0:
        return True
    else:
        return False

assert is_even.__doc__
assert is_even(2)
assert not is_even(3)

# Exercise 3
def is_odd():
    return True

assert is_odd.__doc__
