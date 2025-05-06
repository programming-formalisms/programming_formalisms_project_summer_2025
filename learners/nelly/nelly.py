def is_zero(num):
    """ Returns True if input is number zero"""
    if not isinstance(num, int):
        raise TypeError(f"{num} must be of type int")
    if num == 0:
        return True

    return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)


def is_even(num):
    """ Return true if input is even"""
    if not isinstance(num, int):
        raise TypeError(f"{num} must be of type int")
    
    return num % 2 == 0

assert is_even.__doc__
assert is_even(0)
assert not is_even(1)

def is_odd(num):
    """ Return true if input is odd"""
    if not isinstance(num, int):
        raise TypeError(f"{num} must be of type int")
    
    return num % 2 != 0

assert is_odd.__doc__
assert is_odd(1)
assert not is_odd(2)

try:
    is_odd(2.3)
except TypeError as e:
    assert str(e) == "2.3 must be of type int"




