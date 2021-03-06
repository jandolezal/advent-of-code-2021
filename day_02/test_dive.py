import unittest

from day_02.dive import load_input, Submarine


test_input = load_input('day_02/test_input.txt')
test_output = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]


data = load_input('day_02/input.txt')


class TestDive(unittest.TestCase):
    
    def test_loading_instructions(self):
        self.assertListEqual(test_input, test_output)
    
    @unittest.skip('Logic has changed')
    def test_submarine_with_test_input(self):
        sub = Submarine()
        sub.dive(test_input)
        self.assertEqual(sub.multiply(), 150)
    
    @unittest.skip('Logic has changed')
    def test_submarine(self):
        sub = Submarine()
        sub.dive(data)
        self.assertEqual(sub.multiply(), 2120749)
    
    def test_new_submarine_with_test_input(self):
        sub = Submarine()
        sub.dive(test_input)
        self.assertEqual(sub.multiply(), 900)

    def test_new_submarine(self):
        sub = Submarine()
        sub.dive(data)
        self.assertEqual(sub.multiply(), 2138382217)


if __name__ == '__main__':
    unittest.main()
