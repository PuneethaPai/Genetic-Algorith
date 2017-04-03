import unittest

from nucleotides import Nucleotides


class NucleotidesTest(unittest.TestCase):
    def test_nucleotides_with_same_space_are_equal(self):
        space = set("asdfghjk")
        nucleotides1 = Nucleotides(space)
        nucleotides2 = Nucleotides(space)
        self.assertEquals(nucleotides1, nucleotides2)
        self.assertEquals(nucleotides1.__hash__(), nucleotides2.__hash__())

    def test_nucleotides_with_same_space_are_equal(self):
        space1 = set("asdfghjk")
        space2 = set("qwertyui")
        nucleotides1 = Nucleotides(space1)
        nucleotides2 = Nucleotides(space2)
        self.assertNotEqual(nucleotides1, nucleotides2)
        self.assertNotEqual(nucleotides1.__hash__(), nucleotides2.__hash__())


if __name__ == '__main__':
    unittest.main()