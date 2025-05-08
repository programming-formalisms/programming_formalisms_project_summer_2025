class Position:
    def __init__(self, any_x, any_y):
        self.x = any_x
        self.y = any_y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return 'Position'

a = Position(3.13,927) 
print(a)
print(type(a))
assert str(type(a)) == "<class '__main__.Position'>"
