def divide_by(numerator, denominator):
    """
    Divide two numbers and return the result.
    
    Parameters:
        numerator (float): The numerator.
        denominator (float): The denominator.

    Returns:
        float: The result of the division.
    """
    assert isinstance(numerator, (float))
    assert isinstance(denominator, (float))
    assert denominator != 0, "Denominator cannot be zero"

    return (numerator / denominator)


print(divide_by("banana", 4.0))