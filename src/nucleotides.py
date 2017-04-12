import random

class Nucleotides(object):
    def __init__(self, nucleotides):
        self.nucleotides = nucleotides

    def __eq__(self, other):
        return self.nucleotides == other.nucleotides

    def __hash__(self):
        return ''.join(self.nucleotides).__hash__()

    def create(self, size):
        structure = ''.join(random.sample(self.nucleotides, size))
        return structure
