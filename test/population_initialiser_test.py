import string
import unittest

from nucleotides import Nucleotides
from population_initialise import PopulationInitialise


class PopulationInitialiseTest(unittest.TestCase):
    def test_initialise_population(self):
        nucleotides = Nucleotides(set(string.printable))
        population_initialise = PopulationInitialise(nucleotides)
        population = population_initialise.create(population_size=10, structure_size=500)
        self.assertEquals(population.size, 10)
