import unittest
from day_04.giant_squid import load_input, play


test_input = load_input('day_04/test_input.txt')

data = load_input('day_04/input.txt')


class TestGiantSquid(unittest.TestCase):
    
    def test_loading_input(self):
        draw, boards = test_input
        self.assertEqual(draw, [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1])
        self.assertEqual(len(boards), 3)
        self.assertEqual(boards[0][0], {'value': 22, 'marked': False})
        self.assertEqual(boards[2][-1], {'value': 7, 'marked': False})
    
    def test_play_with_test_input(self):
        draw, boards = test_input
        score = play(draw, boards)
        self.assertEqual(score, 4512)

    def test_playt(self):
        draw, boards = data
        score = play(draw, boards)
        self.assertEqual(score, 8136)

if __name__ == '__main__':
    unittest.main()
