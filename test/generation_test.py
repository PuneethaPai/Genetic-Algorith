import unittest

from mock import Mock

from src.dna import DNA
from src.generation import Generation
from src.population import Population


class GenerationTest(unittest.TestCase):
    def test_generation_for_equality(self):
        mock_population = Mock(spec=Population)
        mock_population.__eq__ = Mock(return_value=True)
        mock_population.__hash__ = Mock(return_value=1)
        generation1 = Generation(1, mock_population)
        generation2 = Generation(1, mock_population)
        self.assertEquals(generation2, generation1)
        self.assertEquals(generation1.__hash__(), generation2.__hash__())

    def test_generation_to_generate_next_generation(self):
        mock_population1 = Mock(spec=Population)
        mock_population2 = Mock(spec=Population)
        mock_population1.next_population = Mock(return_value=mock_population2)
        mock_target_DNA = Mock(spec=DNA)
        generation1 = Generation(1, mock_population1)
        generation2 = generation1.next_generation(mock_target_DNA)
        self.assertEquals(generation2.number, 2)
        self.assertEquals(generation2.population, mock_population2)

    def test_generation_to_retrun_best_fit_people(self):
        best = Mock(spec=DNA)
        fitness = 5
        mock_population = Mock(spec=Population)
        mock_population.best_fit = Mock(return_value=(best, fitness))
        generation = Generation(1, mock_population)
        self.assertEquals((best, fitness), generation.best_fit())
