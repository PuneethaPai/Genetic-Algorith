import unittest

from src.nucleotides import Nucleotides


class NucleotidesTest(unittest.TestCase):
    def test_nucleotides_with_same_space_are_equal(self):
        space = set("asdfghjk")
        nucleotides1 = Nucleotides(space)
        nucleotides2 = Nucleotides(space)
        self.assertEqual(nucleotides1, nucleotides2)
        self.assertEqual(nucleotides1.__hash__(), nucleotides2.__hash__())

    def test_nucleotides_with_different_space_are_unequal(self):
        space1 = set("asdfghjk")
        space2 = set("qwertyui")
        nucleotides1 = Nucleotides(space1)
        nucleotides2 = Nucleotides(space2)
        self.assertNotEqual(nucleotides1, nucleotides2)
        self.assertNotEqual(nucleotides1.__hash__(), nucleotides2.__hash__())

    def test_nucleotides_generate_structure(self):
        space = set("asdfghjkiytfvygjmv")
        nucleotides = Nucleotides(space)
        structure = nucleotides.create(size=10)
        self.assertEqual(len(structure), 10)

    def test_nucleotides_generate_structure_greater_than_available_space(self):
        space = set("asdfghj")
        nucleotides = Nucleotides(space)
        structure = nucleotides.create(size=10)
        self.assertEqual(len(structure), 10)

if __name__ == '__main__':
    unittest.main()