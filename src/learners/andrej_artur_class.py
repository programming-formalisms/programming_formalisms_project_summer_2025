class Parameters:
    def __init__(self, n_bacteria, n_timestamps, gradient_type, bacteria_initialization):
        if isinstance(n_bacteria, int) and n_bacteria >= 0:
            self.n_bacteria = n_bacteria
        else:
            raise TypeError("n_bacteria must be a non-negative integer")
        self._n_bacteria = n_bacteria

        if isinstance(n_timestamps, int) and n_timestamps >= 0:
            self.n_timestamps = n_timestamps
        else:
            raise TypeError("n_timestamps must be a non-negative integer")

        self.gradient_type = gradient_type
        self.bacteria_initialization = bacteria_initialization
    def __str__(self):
        return "this is parameters for teh superbug test"
    def get_n_bacteria(self):
        return self._n_bacteria
    def get_n_timestamps(self):
        return self.n_timestamps
    def get_gradient_type(self):
        return self.gradient_type
    def get_bacteria_init(self):
        return self.bacteria_initialization