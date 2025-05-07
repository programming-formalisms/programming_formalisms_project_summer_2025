
def divide_by(numerator, denominator):
    assert not isinstance(numerator, str)
    assert not isinstance(denominator, str)
    assert(denominator != 0.0)
    return (numerator / denominator)

divide_by(3, "4")