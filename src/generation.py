class Generation(object):

    def __init__(self, number, population):
        self.number = number
        self.population = population

    def __eq__(self, other):
        return self.number == other.number and self.population.__eq__(other)

    def __hash__(self):
        return self.number.__hash__() * self.population.__hash__()

    def next_generation(self, target):
        next_population = self.population.next_population(target)
        return Generation(next_population)
