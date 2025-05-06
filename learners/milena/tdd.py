def is_odd(x):
    if not isinstance(x, (float, int)):
        raise TypeError("input variable is not a number")

    return x % 2 != 0 
    

assert is_odd(3)
assert not is_odd(4.0)

has_thrown = False
try:
    is_odd("3")
except TypeError:
    has_thrown = True

assert has_thrown



def is_probability(x):
    if not isinstance(x, (float, int)):
        raise TypeError("input is not a number")
    
    return x <= 1.0 and x >= 0.0

assert is_probability(0.5)
assert not is_probability(10)

has_thrown = False
try:
    is_probability("0.5")
except TypeError:
    has_thrown = True
assert has_thrown



def is_prime(x):
    if not isinstance(x, int):
        raise TypeError("input is not an integer")
    
    for i in range(2, x):
        if x % i == 0:
            return False 
    
    return True

assert is_prime(5)
assert not is_prime(10)
