class Range:    #largest >= lowest 
    
    def __init__(self, lowest, highest): 
        if not isinstance(lowest, (int, float)) and isinstance(highest, (int, float)):
            raise TypeError("At least One of the arguments is non-numeric")
        self.lowest = lowest
        self.highest = highest
    def get_lowest(self): 
        return self.lowest
    def get_highest(self):
        return self.highest


x = Range(3,10)
assert x.get_lowest() == 3
assert x.get_highest() == 10
Range(100, 10) # Must raise an exception

        
