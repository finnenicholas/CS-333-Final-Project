import unittest
from main import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board_empty(self):
        self.assertEqual(self.game.board, [[' ']*3, [' ']*3, [' ']*3])

if __name__ == '__main__':
    unittest.main()
