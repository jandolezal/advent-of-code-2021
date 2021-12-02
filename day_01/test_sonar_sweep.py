import unittest

from day_01.sonar_sweep import get_increase_count, get_window_increase_count


with open('day_01/test_input.txt') as f:
    test_input = [int(word.strip()) for word in f.readlines()]

test_output = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

with open('day_01/input.txt') as f:
    data = [int(word.strip()) for word in f.readlines()]



class TestSonarSweep(unittest.TestCase):


    def test_sonar_sweep_with_test_data(self):
        self.assertEqual(test_input, test_output)
        increase_count = get_increase_count(test_input)
        self.assertEqual(increase_count, 7)

    def test_sonar_sweep(self):
        increase_count = get_increase_count(data)
        self.assertEqual(increase_count, 1466)
    
    def test_sonar_sweep_sliding_window_with_test_data(self):
        increase_count = get_window_increase_count(test_input)
        self.assertEqual(increase_count, 5)

    def test_sonar_sweep_sliding_window(self):
        increase_count = get_window_increase_count(data)
        self.assertEqual(increase_count, 1491)


if __name__ == '__main__':
    unittest.main()
