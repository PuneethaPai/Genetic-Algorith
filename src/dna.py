import random
import string

from nucleotides import Nucleotides


def generate_mutated_structure(structure, indices, mutation_values):
    for index, nucleotides_value in zip(indices, mutation_values):
        structure[index] = nucleotides_value
    structure = ''.join(structure)
    return structure


class DNA(object):
    nucleotides = Nucleotides(string.printable)

    def __init__(self, structure):
        self.structure = structure

    def __eq__(self, other):
        return self.structure == other.structure

    def __hash__(self):
        return self.structure.__hash__()

    def measure_fitness(self, target):
        fitness = 0
        for this, other in zip(self.structure, target.structure):
            if this == other:
                fitness += 1
        return fitness

    def mutate(self, percentage=10, space_of_possibilities=nucleotides):
        original_structure = list(self.structure)
        mutate_indices = self.__generate_mutable_indices(percentage)
        mutation_values = self.__generate_random_mutation(space_of_possibilities, percentage)
        mutated_structure = generate_mutated_structure(original_structure, mutate_indices, mutation_values)
        return DNA(mutated_structure)

    def crossover(self, other, crossover_points=2):
        crossover_points = self.__generate_crossover_points(crossover_points)
        child_structure = self.__generate_breed(crossover_points, other)
        return DNA(child_structure)

    def __generate_random_mutation(self, nucleotides, percentage):
        mutate_count = self.__calculate_mutate_count(percentage)
        nucleotides_values = nucleotides.create(mutate_count)
        return nucleotides_values

    def __generate_mutable_indices(self, percentage):
        mutate_count = self.__calculate_mutate_count(percentage)
        mutate_indices = random.sample(xrange(len(self.structure)), mutate_count)
        return mutate_indices

    def __calculate_mutate_count(self, percentage):
        mutate_count = len(self.structure) * percentage / 100
        return mutate_count

    def __generate_crossover_points(self, crossover_points):
        crossover_indices = random.sample(xrange(len(self.structure)), crossover_points)
        crossover_indices.sort()
        return crossover_indices

    def __generate_breed(self, indices, other):
        return self.structure[:indices[0]] + \
               other.structure[indices[0]:indices[1]] + \
               self.structure[indices[1]:]
