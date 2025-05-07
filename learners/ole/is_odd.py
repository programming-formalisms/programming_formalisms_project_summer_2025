def is_odd(x):
    '''Return True if x is odd, False if it is even, else return error'''
    if not isinstance(x, int | float | complex):
        print("Not a number?!")
        raise TypeError
    if x%2 == 1:
        return True
    else:
        return False

assert is_odd(3)
assert not is_odd(4)
assert is_odd("hello")