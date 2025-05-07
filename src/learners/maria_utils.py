def is_zero(number):
     """Testing if the number is zero."""
     if not isinstance(number, int):
         raise TypeError("'number' must be of type int.")
     if number == 0:
         return True
     return False

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
