import collections
import random

PERCENT = 100.00


class Population(object):
    kill_percentage = 20
    mutate_percent = 10

    def __init__(self, people):
        self.people = people
        self.size = len(self.people)
        self.fitness = []

    def next_population(self, target):
        self.__calculate_worthiness(target)
        best_people, split_index = self.__kill_unworthy()
        next_generation_people = self.__create_next_generation(best_people, split_index)
        mutated_generation_people = self.__mutate(next_generation_people)
        return Population(mutated_generation_people)

    def best_fit(self):
        if self.fitness == []:
            return self.people[0], -1
        return self.people[0].structure, self.fitness[0]

    def __calculate_worthiness(self, target):
        self.__calculate_fitness(target)
        self.__sort()

    def __create_next_generation(self, best_people, split_index):
        return best_people + self.__create(self.size - split_index, best_people)

    def __kill_unworthy(self):
        split_index = int((PERCENT - self.kill_percentage) / 100 * self.size)
        best_people = self.people[:split_index]
        return best_people, split_index

    def __eq__(self, other):
        identity1 = self.__identify_people()
        identity2 = other.__identify_people()
        return identity1 == identity2

    def __hash__(self):
        return str(self.__identify_people()).__hash__()

    def __calculate_fitness(self, target):
        self.fitness = [DNA.measure_fitness(target) for DNA in self.people]

    def __identify_people(self):
        return collections.Counter(self.people)

    def __sort(self):
        fitness_based = sorted(zip(self.fitness, self.people))
        self.people = [item[1] for item in fitness_based]
        self.fitness = [item[0] for item in fitness_based]
        self.people.reverse()
        self.fitness.reverse()

    def __create(self, required_size, best_people):
        required_population = [self.__child(best_people) for i in xrange(required_size)]
        return required_population

    def __child(self, best_people):
        parents = random.sample(best_people, 2)
        return parents[0].crossover(parents[1])

    def __mutate(self, people):
        mutable_people_index = random.sample(xrange(self.size), self.mutate_percent * self.size / 100)
        for index in mutable_people_index:
            people[index] = people[index].mutate()
        return people
