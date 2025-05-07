def is_even(x):
    'x is input, returns True if x is even, False otherwise'
    a=x/2
    isinstance(a,int)
    return print(a == int(a))


assert is_even.__doc__
assert is_even(2) == True, "Expected True for input 2"
