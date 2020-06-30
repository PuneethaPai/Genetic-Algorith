import string
import unittest

from src.nucleotides import Nucleotides
from src.population_initialise import PopulationInitialise


class PopulationInitialiseTest(unittest.TestCase):
    def test_initialise_population(self):
        nucleotides = Nucleotides(set(string.printable))
        population_initialise = PopulationInitialise(nucleotides)
        population = population_initialise.create(population_size=10, structure_size=500)
        self.assertEqual(population.size, 10)
