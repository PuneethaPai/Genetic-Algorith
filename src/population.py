import collections

PERCENT = 100.00


class Population(object):
    size = 150
    kill_percentage = 20

    def __init__(self, people):
        self.people = people
        self.size = len(self.people)
        self.fitness = []

    def next_population(self, target, kill_percentage=kill_percentage):
        self.__calculate_fitness(target)
        self.__sort()
        split_index = int((PERCENT - kill_percentage) / 100 * self.size)
        next_people = self.people[:split_index]
        return Population(next_people)

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