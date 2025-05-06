

def divide_by(numerator, denominator):
    # Numerator is a floating point number
    assert isinstance(numerator, (float, int))
    # Denominator is a floating point number
    assert isinstance(denominator, (float, int))
    # Numerator is not zero
    assert denominator != 0.
    assert type(numerator) == type(denominator)
    return numerator / denominator

def read_file(filename):
    import os
    # The path to the filename exists
    assert os.path.isfile(filename)
    
    # The file is readable
    assert os.access(filename, os.R_OK)
    
    file = open(filename, "r")
    content = file.read()
    file.close()

    return content

def read_non_empty_file(filename):
    import os
    # The path to the filename exists
    assert os.path.isfile(filename)
    
    # The file is readable
    assert os.access(filename, os.R_OK)
    
    file = open(filename, "r")
    content = file.read()

    # The file is non-empty
    assert content

    file.close()

    return content

print(read_file("feature_r4d1.md"))
read_non_empty_file("empty_file.txt")