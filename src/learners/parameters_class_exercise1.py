class Parameters:
    """
    this class takes four parameters: n_bacteria, n_timesteps, gradient_type, bacteria_initialization
    """
    def __init__(self, any_x, any_y):
        self.x = any_x
        self.y = any_y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return 'Position'