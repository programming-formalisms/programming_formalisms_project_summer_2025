def is_number(x):
    """
    This function tests whether the input variable x is a number or not.
    """
    if isinstance(x, (int, float)):
        return True
    else:
        return False