def read_file(filename):
    import os
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)

    assert isinstance(filename, str)


    file = open(filename, "r")
    content = file.read()
    file.close()
    return content


print(read_file("test2.txt"))