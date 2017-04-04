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

    def test_population_with_different_people_are_not_equal(self):
        dna1 = DNA("asdfghjk")
        dna2 = DNA("qwertyuy")
        dna3 = DNA("zxcvbnqw")
        people1 = [dna1, dna2]
        people2 = [dna3, dna2]
        population1 = Population(people=people1)
        population2 = Population(people=people2)
        self.assertFalse(population1.__eq__(population2))

    def test_fitness_calculatoin_of_people(self):
        people = [DNA("asdfghjk"), DNA("asdfghjk"), DNA("abcdefqw")]
        population = Population(people=people)
        population.calculate_fitness(DNA("abcdefgh"))
        self.assertEquals(population.fitness[0], population.fitness[1])
        self.assertTrue(population.fitness[2] > population.fitness[1])









