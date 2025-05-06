#assert 1 == 2

def divide_by(numerator, denominator):
    assert isinstance(numerator, float)
    assert isinstance(denominator, float)
    assert(denominator != 0.0)
    return (numerator / denominator)

print(divide_by(3.0, 4.0))

def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)

    file = open(filename, "r")
    content = file.read()
    if len(content) == 0:
        raise ValueError("File has no content")
    file.close()
    return content

print(read_file('my text'))
