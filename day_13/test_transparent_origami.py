import unittest
from day_13.transparent_origami import load_input, split, part1



class TestTransparentOrigami(unittest.TestCase):
    
    def test_loading_input(self):
        dots, instructions = load_input('day_13/test_input.txt')
        assert len(dots) == 18
        assert dots[0] == (3,0)
        assert dots[-1] == (2,14)
        assert len(instructions) == 2
        assert instructions[-1] == ('x', 5)
    

    def test_part_1_with_test_data(self):
        dots, instructions = load_input('day_13/test_input.txt')
        new_dots = split(dots, 'y', 7)
        assert len(new_dots) == 17

        another_dots = split(new_dots, 'x', 5)
        assert len(another_dots) == 16
    
    def test_part_1_with_test_data_in_one_go(self):
        dots, instructions = load_input('day_13/test_input.txt')
        for axis, fold_index in instructions:
            dots = split(dots, axis, fold_index)
        assert len(dots) == 16

    def test_part_1(self):
        new_dots = part1()
        assert len(new_dots) == 710


if __name__ == '__main__':
    unittest.main()
