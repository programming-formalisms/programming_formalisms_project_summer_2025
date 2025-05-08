def get_digits(*nums):
    """
        Input: one number to be split in digits 
        Returns the number split into a list of digits, e.g. 314 become [3, 1, 4] If the input is not one integer, or is negative, a TypeError is raised
    """
    if len(nums) > 1:
        raise TypeError(f"Expected one input but got {len(nums)}")
    if not isinstance(nums[0], int):
        raise TypeError("Please only provide integer value")
    num = int(nums[0])
    if num < 0:
        raise TypeError(f"Please only provide a positive integer")
    
    return [int(x) for x in str(num)]

assert get_digits(314) == [3,1,4]
assert get_digits(1) == [1]
try:
    get_digits(12, 34)
except TypeError as e:
    assert str(e) == "Expected one input but got 2"
try:
    get_digits(-5)
except TypeError as e:
    assert str(e) == "Please only provide a positive integer"
try:
    get_digits('test')
except TypeError as e:
    assert str(e) == "Please only provide integer value"

