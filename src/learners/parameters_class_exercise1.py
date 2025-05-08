class Position:
    def __init__(self, any_x, any_y):
        self.x = any_x
        self.y = any_y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return 'Position'