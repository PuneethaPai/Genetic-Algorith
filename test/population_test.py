import unittest

from dna import DNA
from population import Population


class PopulationTest(unittest.TestCase):
    def test_population_with_same_people_are_equal(self):
        people = [DNA("asdfghjk"), DNA("asdfghjk")]
        population1 = Population(people=people)
        population2 = Population(people=people)
        self.assertEquals(population1, population2)
        self.assertEquals(population1.__hash__(), population2.__hash__())

    def test_population_to_generate_improved_next_population(self):
        people = [DNA("asdfghjk"), DNA("qwerthjk"), DNA("abcdefqw")] * 50
        population = Population(people=people)
        next_population = population.next_population(target=DNA("abcdefqw"))
        self.assertNotEqual(population, next_population)
        self.assertEqual(len(population.people), len(next_population.people))

    def test_population_to_produce_best_fit(self):
        best = DNA("asdfghjk")
        people = [best, DNA("qwerthjk"), DNA("abcdefqw")] * 50
        population = Population(people=people)
        self.assertEquals(best, population.best_fit())