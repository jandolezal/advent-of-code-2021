import unittest
from day_05.hydrothermal_venture import load_input, line_from_both_ends, make_lines, build_diagram, calculate_points


class TestHydrothermalVenture(unittest.TestCase):
    
    def test_loading_input(self):
        test_input = load_input('day_05/test_input.txt')
        assert test_input == [[(0, 9), (5, 9)], [(8, 0), (0, 8)], [(9, 4), (3, 4)], [(2, 2), (2, 1)], [(7, 0), (7, 4)], [(6, 4), (2, 0)], [(0, 9), (2, 9)], [(3, 4), (1, 4)], [(0, 0), (8, 8)], [(5, 5), (8, 2)]]

    def test_line_from_both_ends(self):
        test_input = load_input('day_05/test_input.txt')
        assert line_from_both_ends(test_input[0]) == [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
        assert line_from_both_ends(test_input[3]) == [(2, 1), (2, 2)]
    
    def test_make_lines(self):
        test_input = load_input('day_05/test_input.txt')
        assert make_lines(test_input) == [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (2, 1), (2, 2), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (0, 9), (1, 9), (2, 9), (1, 4), (2, 4), (3, 4)]

    def test_calculate_points_with_test_data(self):
        data = load_input('day_05/test_input.txt')
        lines = make_lines(data)
        diagram = build_diagram(lines)
        points = calculate_points(diagram)
        assert points == 5

    def test_calculate_points(self):
        data = load_input('day_05/input.txt')
        lines = make_lines(data)
        diagram = build_diagram(lines)
        points = calculate_points(diagram)
        assert points == 7085

if __name__ == '__main__':
    unittest.main()
