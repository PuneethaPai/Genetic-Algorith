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


if __name__ == '__main__':
    unittest.main()
