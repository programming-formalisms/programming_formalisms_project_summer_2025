class Position:
    def __init__(self, any_x, any_y):
        if not (isinstance(any_x, [int, float]) and isinstance(any_y, [int, float])):
            raise TypeError("At least One of the positional argument is non-numeric")

        self.x = any_x
        self.y = any_y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return 'Position'
