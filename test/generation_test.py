import unittest

from mockito import mock, when

from src.dna import DNA
from src.generation import Generation
from src.population import Population


class GenerationTest(unittest.TestCase):
    def test_generation_for_equality(self):
        mock_population = mock(spec=Population)
        # when(mock_population).__eq__(...).thenReturn(True)
        # when(mock_population).__hash__(...).thenReturn(1)
        generation1 = Generation(1, mock_population)
        generation2 = Generation(1, mock_population)
        self.assertEqual(generation2, generation1)
        self.assertEqual(generation1.__hash__(), generation2.__hash__())

    def test_generation_to_generate_next_generation(self):
        mock_population1 = mock(spec=Population)
        mock_population2 = mock(spec=Population)
        when(mock_population1).next_population(...).thenReturn(mock_population2)
        mock_target_DNA = mock(spec=DNA)
        generation1 = Generation(1, mock_population1)
        generation2 = generation1.next_generation(mock_target_DNA)
        self.assertEqual(generation2.number, 2)
        self.assertEqual(generation2.population, mock_population2)

    def test_generation_to_retrun_best_fit_people(self):
        best = mock(spec=DNA)
        fitness = 5
        mock_population = mock(spec=Population)
        when(mock_population).best_fit(...).thenReturn((best, fitness))
        generation = Generation(1, mock_population)
        self.assertEqual((best, fitness), generation.best_fit())
