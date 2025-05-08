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

class Date:
    def __init__(self, y:int,m:int,d:int):
      self.year = y
      self.month = m
      self.day = d
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

class Temperature:
    def __init__(self, temp:float, temp_corrected:float):
      self.temp = temp
      self.temp_corrected = temp_corrected
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

class DataPoint:
    def __init__(self, any_position, any_velocity):
      self.position = any_position
      self.velocity = any_velocity
    def __str__(self):
        return (
            "Position: " + str(self.position)  + ", "
            + "velocity" + str(self.velocity)
        )