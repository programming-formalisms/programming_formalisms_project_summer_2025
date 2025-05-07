#Ex 1
def is_zero(x):
    '''Determines if the input value is zero'''
    if not isinstance(x,int):
        raise TypeError("Input must be a number.")
    if x==0:
        return True

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

#Ex 2