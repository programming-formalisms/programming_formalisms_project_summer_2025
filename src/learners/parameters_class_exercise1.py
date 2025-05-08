class Parameters:
    """
    this class takes four parameters: n_bacteria, n_timesteps, gradient_type, bacteria_initialization
    """
    def __init__(self, n_bacteria, n_timesteps, gradient_type, bacteria_initialization):
        self.n_bacteria = n_bacteria
        self.n_timesteps = n_timesteps
        self.gradient_type = gradient_type
        self.bacteria_initialization = bacteria_initialization
    def __str__(self):
        return f'Number of bacteria: {self.n_bacteria} \nNumber of timesteps: {self.n_timesteps} \nGradient type: {self.gradient_type} \nBacteria initialization: {self.bacteria_initialization}'
    def __repr__(self):
        return 'Parameters'