import unittest
from day_03.binary_diagnostic import load_input, compute_rate


test_input = load_input('day_03/test_input.txt')
test_output = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


data = load_input('day_03/input.txt')


class TestBinaryDiagnostic(unittest.TestCase):
    
    def test_loading_instructions(self):
        self.assertListEqual(test_input, test_output)
    
    def test_compute_rate_gamma(self):
        gamma_rate = compute_rate(test_input, 'gamma')
        self.assertEqual(gamma_rate, 22)

    def test_compute_rate_epsilon(self):
        epsilon_rate = compute_rate(test_input, 'epsilon')
        self.assertEqual(epsilon_rate, 9)

    def test_power_consumption_first_part(self):
        gamma_rate = compute_rate(data, 'gamma')
        epsilon_rate = compute_rate(data, 'epsilon')
        power_consumption = gamma_rate * epsilon_rate
        self.assertEqual(power_consumption, 841526)


if __name__ == '__main__':
    unittest.main()
