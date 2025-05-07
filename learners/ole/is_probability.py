def is_probability(x):
    if isinstance(x, int | float | complex):
        raise TypeError
    if x >= 0 and x <= 1:
        return True
    else:
        return False
    
assert is_probability(1, 0, 0.5)
assert is_probability(0)
assert is_probability(1)
assert not is_probability(1.5)
