import unittest

from day_15.chiton import load_input, dijkstra


class TestChiton(unittest.TestCase):
    
    def test_dijkstra_with_test_input(self):
        data = load_input('day_15/test_input.txt')
        costs = dijkstra(data)
        self.assertEqual(costs[-1][-1], 40)
    
    def test_dijkstra(self):
        data = load_input('day_15/input.txt')
        costs = dijkstra(data)
        self.assertEqual(costs[-1][-1], 707) 


if __name__ == '__main__':
    unittest.main()
