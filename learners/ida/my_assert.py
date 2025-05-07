# Exercise 1
#assert 1 == 2

# Exercise 2
def divide_by(numerator, denominator):
    assert isinstance(numerator, float)
    assert isinstance(denominator, float)
    assert denominator != 0.0
    return (numerator / denominator)

print(divide_by(3.0, 4.0))

# Exercise 3
def read_file(filename):
    #import os
    #assert os.path.isfile(filename)
    #assert os.access(filename, os.R_OK)
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

print(read_file("/Users/idake859/Documents/programming_formalisms_project_summer_2025/learners/ida/feature_list.md"))
print(read_file("/Users/idake859/Documents/programming_formalisms_project_summer_2025/learners/ida/test.txt"))

# Adding a comment