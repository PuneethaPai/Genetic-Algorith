import collections


class Population(object):
    size = 150
    kill_percentage = 20

    def __init__(self, people):
        self.people = people
        self.size = len(self.people)
        self.fitness = []

    def __eq__(self, other):
        identity1 = self.__identify_people()
        identity2 = other.__identify_people()
        return identity1 == identity2

    def __hash__(self):
        return str(self.__identify_people()).__hash__()

    def next_population(self, target, kill_percentage=kill_percentage):
        self.calculate_fitness(target)
        self.sort()
        return Population(self.people[:(100 - kill_percentage) * self.size])

    def __identify_people(self):
        return collections.Counter(self.people)
