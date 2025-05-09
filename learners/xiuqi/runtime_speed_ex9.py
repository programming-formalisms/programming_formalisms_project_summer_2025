import cProfile

def main():
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
        return (phenotype + 5) % 10  # Imagine something complex here

    n_individuals = 1000
    population = []
    for i in range(n_individuals):
        population.append(Individual(i % 10))
    assert len(population) == n_individuals

    for i in range(n_individuals):
        phenotype = population[i].get_phenotype()
        fitness = calc_fitness(phenotype)
        # Do something with the fitness

if __name__ == "__main__":
    cProfile.run('main()', sort='time')
