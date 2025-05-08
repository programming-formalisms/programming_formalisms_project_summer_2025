def is_zero(number):
    """Testing if the number is zero."""
    if not isinstance(number, int):
        raise TypeError("'number' must be of type int.")
    if number == 0:
        return True
    return False

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def is_datetime(x):
    from datetime import datetime
    if not isinstance(x,str):
        raise TypeError("The input must be a string.")
    if len(x) != 16:
        return False
    try:
        datetime.strptime(x, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False