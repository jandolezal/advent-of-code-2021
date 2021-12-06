import unittest
from day_06.lanternfish import load_input, simulate


class TestLanternfish(unittest.TestCase):
    
    def test_loading_input(self):
        test_input = load_input('day_06/test_input.txt')
        assert test_input == [3,4,3,1,2]
    
    def test_simulate_with_test_input(self):
        test_input = load_input('day_06/test_input.txt')
        count, fishes = simulate(test_input, 18)
        assert count == 26

    def test_simulate(self):
        test_input = load_input('day_06/input.txt')
        count, fishes = simulate(test_input, 80)
        assert count == 365131

if __name__ == '__main__':
    unittest.main()
