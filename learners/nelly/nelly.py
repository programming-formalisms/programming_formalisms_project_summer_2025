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


def is_probability(num):
    """ Return true if input is between 0.0 and 1.0"""
    if not isinstance(num, (float, int)):
        raise TypeError(f"{num} must be of type float or int")

    return 0.0 <= num <= 1.0
    
assert is_probability(0.75)
assert is_probability(1)
assert not is_probability(1.01)


def is_prime(*nums):
    """ Return true if input is a prime number"""
    if len(nums) > 1:
        raise Exception(f"Only one argument expected but got {len(nums)}")
    if not isinstance(nums[0], (float, int)):
        raise TypeError(f"{num} must be of type float or int")
    
    n = nums[0]
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

assert is_prime(7)
assert not is_prime(4)
try:
    is_prime(1, 0.3)
except Exception as e:
    assert str(e) == "Only one argument expected but got 2"
