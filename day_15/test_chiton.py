import unittest

from day_15.chiton import load_input, dijkstra, inflate_data


class TestChiton(unittest.TestCase):
    
    def test_dijkstra_with_test_input(self):
        data = load_input('day_15/test_input.txt')
        costs = dijkstra(data)
        self.assertEqual(costs[-1][-1], 40)
    
    def test_dijkstra(self):
        data = load_input('day_15/input.txt')
        costs = dijkstra(data)
        self.assertEqual(costs[-1][-1], 707)

    def test_dijkstra_with_inflated_test_input(self):
        data = load_input('day_15/test_input.txt')
        inflated_data = inflate_data(data)
        costs = dijkstra(inflated_data)
        self.assertEqual(costs[-1][-1], 315)
    
    def test_dijkstra_with_inflated_data(self):
        data = load_input('day_15/input.txt')
        inflated_data = inflate_data(data)
        costs = dijkstra(inflated_data)
        self.assertEqual(costs[-1][-1], 2942) 

if __name__ == '__main__':
    unittest.main()
