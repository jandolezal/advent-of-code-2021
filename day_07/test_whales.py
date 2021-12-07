import unittest
from day_07.whales import load_input


class TestWhales(unittest.TestCase):
    
    def test_loading_input(self):
        test_input = load_input('day_07/test_input.txt')


if __name__ == '__main__':
    unittest.main()
