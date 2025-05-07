def get_digits(x): 
    '''Convert an integer to a list of integers.'''
    if not isinstance(x, int):
        msg = "Input should be an integer."
        raise TypeError(msg)
    elif x < 0:
        msg = "Input should be positive."
        raise TypeError(msg)
    else:
        integer_list = [int(a) for a in str(x)]
        return(integer_list)