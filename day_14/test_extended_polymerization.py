from array import array
import collections
import unittest

from day_14.extended_polymerization import load_input, make_steps



class TestExtendedPolymerization(unittest.TestCase):
    
    def test_loading_input(self):
        template, rules = load_input('day_14/test_input.txt')
        self.assertEqual(template, array('b', [78, 78, 67, 66]))
        self.assertDictContainsSubset({(ord('C'), ord('H')): ord('B'), (ord('C'), ord('N')): ord('C')}, rules)
    
    def test_make_steps_with_test_input(self):
        template, rules = load_input('day_14/test_input.txt')
        final_template = make_steps(template, rules, steps=10)

        c = collections.Counter(final_template)
        most_common = c.most_common()
        most = most_common[0][1]
        least = most_common[-1][1]

        self.assertEqual(most - least, 1588)


if __name__ == '__main__':
    unittest.main()
