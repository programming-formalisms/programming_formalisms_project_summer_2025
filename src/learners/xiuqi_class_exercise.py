class Position:
    def __init__(self, any_x, any_y):
      self.x = any_x
      self.y = any_y
    def __repr__(self):
        return "Position"
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

assert len(str(Position(1.2, 3.4))) > 0
assert len(type(Position(1.2, 3.4))) > 0
assert Position(1.2, 3.4).x == 1.2
assert Position(1.2, 3.4).y == 3.4