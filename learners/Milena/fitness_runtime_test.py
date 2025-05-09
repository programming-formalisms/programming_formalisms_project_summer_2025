class Individual:
    def __init__(self, phenotype):
        """Genotype, a value from 0 to and including 9"""
        assert isinstance(phenotype, int)
        assert phenotype >= 0
        assert phenotype <= 9
        self._phenotype = phenotype
    def get_phenotype(self):
        """Genotype, a value from 0 to and including 9"""
        return self._phenotype

def calc_fitness(phenotype):
    """Complex calculation."""
    assert isinstance(phenotype, int)
    assert phenotype >= 0
    assert phenotype <= 9
    return (phenotype + 5) % 10 # Imagine something complex here

def create_phenotype_fitness_lookup_table():
    lut = dict()
    for phenotype in range(10):
        assert phenotype >= 0
        assert phenotype <= 9
        lut[phenotype] = calc_fitness(phenotype)
    return lut

def make_population(n_individuals):
    population = []
    for i in range(n_individuals):
        population.append(Individual(i % 10))
    assert len(population) == n_individuals
    return population

def calculate_fitness(population):
        # Calculate the fitness each time
    for i in range(len(population)):
        phenotype = population[i].get_phenotype()
        print(phenotype)
        fitness = calc_fitness(phenotype) # Complex calculation
        # Do something with the fitness
        return fitness
    
def calculate_fitness2(population):
    phenotype_fitness_lookup_table = create_phenotype_fitness_lookup_table()
    for i in range(len(population)):
        phenotype = population[i].get_phenotype()
        fitness = phenotype_fitness_lookup_table[phenotype] # Look up the value
        # Do something with the fitness
        return fitness

def do_it():
    population = make_population(n_individuals=int(1e6))
    fitness = calculate_fitness(population)
    fitness2 = calculate_fitness2(population)


import cProfile
cProfile.run('do_it()')