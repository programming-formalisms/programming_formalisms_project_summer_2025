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

        all_measurements = []
        for measurement in infile_list:
            year, month, day, temp, temp_corrected, loc_id = measurement.strip().split()
            measurement_date = Date(year, month, day)
            measurement_temp = Temperature(temp, temp_corrected)
            all_measurements.append(DataPoint(measurement_date, measurement_temp, loc_id))

    return all_measurements
    # if len(infile_list) >0:
    #     return True

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
        return f'measured temperature: {self.temp}°C, corrected for urban effect: {self.temp_corrected}°C'

class DataPoint:
    def __init__(self, measurement_date:Date, measurement_temperature:Temperature, metadata_id:int):
      self.date = measurement_date
      self.temp = measurement_temperature
      self.loc_id = metadata_id
    def __str__(self):
        return (
            f"Temperature on {self.date}:\n{self.temp}\nlocation ID: {str(self.loc_id)}"
        )

#test_result = read_data("/Users/xiuqi.ji/Library/CloudStorage/OneDrive-KarolinskaInstitutet/NAISS/Programming_Formalisms/programming_formalisms_project_summer_2025/data/uppsala_tm_1722-2022.dat")
#print(test_result[0])