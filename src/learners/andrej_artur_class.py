class Parameters:
    def __init__(self, n_bacteria, n_timestamps, gradient_type, bacteria_initialization):
        self.n_bacteria = n_bacteria
        self.n_timestamps = n_timestamps
        self.gradient_type = gradient_type
        self.bacteria_initialization = bacteria_initialization
    def __str__(self):
        return "this is parameters for teh superbug test"
    def get_n_bacteria(self):
        return self.n_bacteria
    def get_n_timestamps(self):
        return self.n_timestamps
    def get_gradient_type(self):
        return self.gradient_type
    def get_bacteria_init(self):
        return self.bacteria_initialization