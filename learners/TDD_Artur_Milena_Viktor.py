def is_even(x):
    """
    Checks if a number is even.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an integer or float.")
    
    # if x % 2 != 0:
    #    return False
    # else:
    #    return True
    
    return x % 2 == 0

assert is_even.__doc__
assert is_even(2)
assert not is_even(3)
# assert is_even("2")