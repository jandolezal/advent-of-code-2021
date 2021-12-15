import collections
import unittest

from day_14.extended_polymerization import load_input, make_steps


class TestExtendedPolymerization(unittest.TestCase):
    
    def test_loading_input(self):
        template, rules = load_input('day_14/test_input.txt')
        self.assertEqual(template, collections.Counter({('N', 'N'): 1, ('N', 'C'): 1, ('C', 'B'): 1}))
        self.assertDictContainsSubset({('C', 'H'): 'B', ('C', 'N'): 'C'}, rules)


if __name__ == '__main__':
    unittest.main()
