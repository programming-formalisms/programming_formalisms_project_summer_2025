"""Class and helper functions on the computational experiment."""

def read_data(filepath:str):
    """Read the weather data from file."""

    # check if file exists at specified path
    import os 
    if not os.path.isfile(filepath):
        raise RuntimeError("file not found! Incorrect filepath?")
    
    # see if file can be read into a list (each element is one line)
    with open(filepath, "r") as infile:
        infile_list = infile.readlines()
    
    if len(infile_list) >0:
        return True
    