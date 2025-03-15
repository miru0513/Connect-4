import unittest

from Board import Board
from Game import Game


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_is_empty(self):
        self.assertTrue(all(cell == " " for row in self.board.matrixboard for cell in row))

    def test_valid_move(self):
        self.assertTrue(self.board.is_valid_move(0))
        self.assertFalse(self.board.is_valid_move(7))

    def test_drop_piece(self):
        self.assertTrue(self.board.drop_piece(0, "X"))
        self.assertEqual(self.board.matrixboard[5][0], "X")

    def test_check_winner_horizontal(self):
        for col in range(4):
            self.board.drop_piece(col, "X")
        self.assertTrue(self.board.check_winner("X"))

    def test_check_winner_vertical(self):
        for _ in range(4):
            self.board.drop_piece(0, "X")
        self.assertTrue(self.board.check_winner("X"))

    def test_check_winner_diagonal_positive_slope(self):
        for i in range(4):
            for _ in range(i):
                self.board.drop_piece(i, "O")
            self.board.drop_piece(i, "X")
        self.assertTrue(self.board.check_winner("X"))

    def test_is_full(self):
        for col in range(self.board.columns):
            for _ in range(self.board.rows):
                self.board.drop_piece(col, "X")
        self.assertTrue(self.board.is_full())


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_switch_player(self):
        self.assertEqual(self.game.switch_player(self.game.human), self.game.computer)
        self.assertEqual(self.game.switch_player(self.game.computer), self.game.human)




if __name__ == "__main__":
    unittest.main()
