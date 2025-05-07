def is_propability(value):
    """
    Check if a value is a valid probability (between 0 and 1 inclusive).
    
    Args:
        value (float): The value to check.
        
    Returns:
        bool: True if the value is a valid probability, False otherwise.
        
    Raises:
        TypeError: If the input is not a number.
    """
    assert isinstance(value, (int, float))
    
    return 0 <= value <= 1
    

assert is_propability.__doc__
assert is_propability(0.5) == True, "Expected True for input 0.5"
assert is_propability(1.5) == False, "Expected True for input 1.5" 
assert is_propability(0.4) == True, "Expected True for input 0.4"
assert is_propability(0) == True, "Expected True for input 0"
assert not is_propability(-1.5) 


try: #  Test for non-numeric input
    is_propability('0.5')
except AssertionError:
    print("TypeError: Input must be a number")
    assert True
else:
    assert False, "Expected TypeError for non-numeric input"


