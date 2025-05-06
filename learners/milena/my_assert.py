# assert 1 == 2

def divide_by(numerator, denominator):
    assert isinstance(numerator, (float, int))
    assert isinstance(denominator, (float, int))
    assert type(numerator) == type(denominator)
    assert denominator != 0.0
    return (numerator / denominator)

# division = divide_by(1.2, 3.4)
# division = divide_by(3, 4)
# print(division)


def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)

    file = open(filename, "r")
    content = file.read()

    assert len(content) > 0
    if len(content) == 0:
        raise ValueError("File has no content")

    file.close()
    return content

