import random


class Nucleotides(object):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides

    def __eq__(self, other):
        return self.nucleotides == other.nucleotides

    def __hash__(self):
        return ''.join(self.nucleotides).__hash__()

    def create(self, size):
        space = self.__get_space_for(size)
        structure = ''.join(random.sample(space, size))
        return structure

    def __get_space_for(self, size):
        space = list(self.nucleotides)
        multiple = size / len(self.nucleotides) + 1
        space *= multiple
        random.shuffle(space)
        return space
