
def is_prime(value):
    """Checks if the number is prime"""
    assert isinstance(value, int)
    if value % 2 == 0:
        return False
    for i in range(3,value,2):
        if value % i == 0:
            return False
    return True
        

assert is_prime.__doc__

assert not is_prime(4)
assert is_prime(7)
assert is_prime(233)

try:
    is_prime("0.5")
except AssertionError:
    assert True
else:
    assert False

try:
    is_prime(0.5)
except AssertionError:
    assert True
else:
    assert False

