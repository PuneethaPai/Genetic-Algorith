import random

from nucleotides import Nucleotides


class DNA(object):

    def __init__(self, structure):
        self.structure = structure

    def __eq__(self, other):
        return self.structure == other.structure

    def __hash__(self):
        return self.structure.__hash__();

    def measure_fitness(self, target):
        fitness = 0
        for this, other in zip(self.structure, target.structure):
            if this == other:
                fitness += 1
        return fitness

    def mutate(self, percentage, nucleotides):
        mutated_structure = list(self.structure)
        mutate_count = len(self.structure) * percentage / 100
        mutate_indices = random.sample(xrange(len(self.structure)), mutate_count)
        nucleotides_values = random.sample(nucleotides.nucleotides, mutate_count)
        for index, nucleotides_value in zip(mutate_indices, nucleotides_values):
            mutated_structure[index] = nucleotides_value
        mutated_structure = ''.join(mutated_structure)
        return DNA(mutated_structure)

