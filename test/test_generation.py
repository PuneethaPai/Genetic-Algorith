import unittest

from mock import Mock

from generation import Generation
from population import Population


class GenerationTest(unittest.TestCase):
    
    def test_generation_for_equality(self):
        mock_population = Mock(spec=Population)
        mock_population.__eq__ = Mock(return_value=True)
        mock_population.__hash__ = Mock(return_value=1)
        generation1 = Generation(1, mock_population)
        generation2 = Generation(1, mock_population)
        self.assertEquals(generation2, generation1)
        self.assertEquals(generation1.__hash__(), generation2.__hash__())