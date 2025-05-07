# Ex 1
# assert 1 == 2

# Ex 2
def divide_by(numerator, denominator):
    assert isinstance(numerator,(float,int))
    assert isinstance(denominator,(float,int))
    assert denominator!=0
    return (numerator / denominator)

divide_by(3,4)

# Ex 3
import os
def read_file(filename):
    # file path should exist
    assert os.path.exists(filename)
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

# Ex 4
def read_non_empty_file(filename):
    import os
    assert os.path.isfile(filename) # file path exists
    assert os.access(filename, os.R_OK) # file is readable
    file = open(filename, "r")
    content = file.read()
    # The file should be non empty
    assert len(content)>0
    file.close()
    return content