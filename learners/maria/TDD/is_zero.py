def is_zero(x):
    "x is input, returns True if x is zero, False otherwise"
    return x == 0

assert is_zero.__doc__
assert is_zero(0) == True, "Expected True for input 0"
assert is_zero(0)  
assert is_zero(1) == False, "Expected False for input 1"
assert not is_zero(1) == True, "Expected False for input -1"
