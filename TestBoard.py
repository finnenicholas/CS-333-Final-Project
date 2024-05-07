import unittest

from main import *


class TestBoard(unittest.TestCase):

  def test_accross_win(self):
    self.assertTrue(
        check_for_win(
            board=[["O", "O", "O"], ["X", "X", " "], [" ", "X", " "]]), True)

  def test_vertical_win(self):
    self.assertTrue(
        check_for_win(
            board=[["X", "O", "X"], ["X", "O", " "], [" ", "O", " "]]), True)

  def test_diagonal_win(self):
    self.assertTrue(
        check_for_win(
            board=[["X", "O", "X"], ["X", "X", " "], [" ", "O", "X"]]), True)

  def test_check_for_stalemate(self):
    self.assertTrue(
        check_for_stalemate(
            board=[["X", "O", "X"], ["X", "X", "O"], ["O", "X", "0"]]), True)

  def test_place_mark_player_2(self):
    self.assertTrue(
        place_mark(1, [["X", "O", "X"], ["X", "X", " "], [" ", "O", "X"]],
                   "12"), [["X", "O", "X"], ["X", "X", "X"], [" ", "O", "X"]])

  def test_place_mark_player_1(self):
    self.assertTrue(
        place_mark(0, [["X", "O", "X"], ["X", "X", "O"], [" ", "O", "X"]],
                   "12"), [["X", "O", "X"], ["X", "X", "O"], [" ", "O", "X"]])

  def test_validate_move(self):
    self.assertTrue(
        validate_move(1, [["X", "O", "X"], ["X", "X", " "], ["X", "O", " "]],
                      "12"), True)

  def test_validate_move_edge_case(self):
    self.assertFalse(
        validate_move(1, [["X", "O", "X"], ["X", "X", " "], ["X", "O", " "]],
                      "33"), True)
    self.assertFalse(
      validate_move(1, [["X", "O", "X"], ["X", "X", " "], ["X", "O", " "]],
                    "aa"), True)

