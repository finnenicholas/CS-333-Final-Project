import unittest
from main import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board_empty(self):
        self.assertEqual(self.game.board, [[' ']*3, [' ']*3, [' ']*3]) # That's cool how you can do the *3

    def test_place_mark(self):
        self.assertTrue(self.game.place_mark(0, 0))
        self.assertEqual(self.game.board[0][0], 'O')
        self.game.current_player = 1
        self.assertTrue(self.game.place_mark(0, 1))
        self.assertEqual(self.game.board[0][1], 'X')

    def test_place_mark_on_taken_spot(self):
        self.game.place_mark(0, 0)
        self.assertFalse(self.game.place_mark(0, 0))

    def test_validate_move_valid(self):
        self.assertTrue(self.game.validate_move(0, 0))

    def test_validate_move_invalid(self):
        self.assertFalse(self.game.validate_move(-1, 0))
        self.assertFalse(self.game.validate_move(3, 3))

    def test_check_for_win_horizontal(self):
        self.game.board = [['O', 'O', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.game.check_for_win())

    def test_check_for_win_vertical(self):
        self.game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(self.game.check_for_win())

    def test_check_for_win_diagonal(self):
        self.game.board = [['O', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'O']]
        self.assertTrue(self.game.check_for_win())

    def test_check_for_stalemate(self):
        self.game.board = [['O', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]
        self.assertTrue(self.game.check_for_stalemate())

    def test_no_stalemate_if_moves_left(self):
        self.game.board = [['O', 'X', 'O'], ['O', ' ', 'X'], ['X', 'O', 'X']]
        self.assertFalse(self.game.check_for_stalemate())

if __name__ == '__main__':
    unittest.main()
