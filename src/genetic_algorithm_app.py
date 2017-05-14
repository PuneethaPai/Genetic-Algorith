import string


from dna import DNA
from generation import Generation
from nucleotides import Nucleotides
from population_initialise import PopulationInitialise


class StartApp(object):
    def __init__(self, population_size, kill_percentage, mutate_percentage):
        self.population_size = population_size
        self.kill_percentage = kill_percentage
        self.mutate_percentage = mutate_percentage

    def _initialise(self, target_string):
        target_length = len(target_string)
        nucleotides = Nucleotides(string.printable)
        DNA.nucleotides = nucleotides
        population_initialise = PopulationInitialise(nucleotides)
        first_population = population_initialise.create(population_size=self.population_size, structure_size=target_length)
        first_generation = Generation(1, first_population)
        return [first_generation]

    def run(self, target_string):
        self.target = DNA(target_string)
        self.generations = self._initialise(target_string)
        result = []
        while True:
            next_generation = self.generations[-1].next_generation(self.target)
            result.append(self.generations[-1].best_fit())
            if result[-1][0] == target_string:
                break
            self.generations.append(next_generation)
        return result