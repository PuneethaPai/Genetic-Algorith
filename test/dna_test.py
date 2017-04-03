import string
import unittest

from dna import DNA
from nucleotides import Nucleotides


class DNA_Test(unittest.TestCase):
    nucleotides = Nucleotides(set(string.printable))

    def test_dna_with_same_structure_are_equal(self):
        dna1 = DNA("abcd")
        dna2 = DNA("abcd")
        self.assertEquals(dna1, dna2)
        self.assertEquals(dna1.__hash__(), dna2.__hash__())

    def test_dna_with_different_structure_are_not_equal(self):
        dna2 = DNA("abcde")
        self.assertNotEqual(DNA("abcd"), dna2)
        self.assertNotEqual(DNA("abcd").__hash__(), dna2.__hash__())

    def test_fitness_of_dna(self):
        dna1 = DNA("abcd")
        dna2 = DNA("abef")
        self.assertEqual(dna1.measure_fitness(dna2), 2)

    def test_dna_mutation(self):
        dna = DNA("asdfghjkzxcvbnm")
        mutated_dna = dna.mutate(20, self.nucleotides)
        self.assertNotEqual(dna, mutated_dna)
        self.assertEquals(len(dna.structure), len(mutated_dna.structure))

    def test_dna_crossover(self):
        dna1 = DNA("asdfghjkl")
        dna2 = DNA("qwertyuio")
        crossover_points = 2
        child1 = dna1.crossover(dna2, crossover_points)
        child2 = dna2.crossover(dna1, crossover_points)
        self.assertNotEqual(child1, child2)
        self.assertEqual(len(child1.structure), len(child2.structure))

if __name__ == '__main__':
    unittest.main()
