from src.dna import DNA
from src.population import Population


class PopulationInitialise(object):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides
        DNA.nucleotides = nucleotides

    def create(self, population_size=100, structure_size=10):
        people = [DNA(self.nucleotides.create(size=structure_size)) for i in range(population_size)]
        return Population(people=people)
