import random


def generate_mutated_structure(structure, indices, mutation_values):
    for index, nucleotides_value in zip(indices, mutation_values):
        structure[index] = nucleotides_value
    structure = ''.join(structure)
    return structure


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
        original_structure = list(self.structure)
        mutate_indices = self.generate_mutable_indices(percentage)
        mutation_values = self.generate_random_mutation(nucleotides, percentage)
        mutated_structure = generate_mutated_structure(original_structure, mutate_indices, mutation_values)
        return DNA(mutated_structure)

    def generate_random_mutation(self, nucleotides, percentage):
        mutate_count = self.calculate_mutate_count(percentage)
        nucleotides_values = random.sample(nucleotides.nucleotides, mutate_count)
        return nucleotides_values

    def generate_mutable_indices(self, percentage):
        mutate_count = self.calculate_mutate_count(percentage)
        mutate_indices = random.sample(xrange(len(self.structure)), mutate_count)
        return mutate_indices

    def calculate_mutate_count(self, percentage):
        mutate_count = len(self.structure) * percentage / 100
        return mutate_count
