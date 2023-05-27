import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_player_move(self):
        self.assertTrue(self.game.player_move(0, 0))
        self.assertFalse(self.game.player_move(0, 0))

    def test_computer_move(self):
        self.game.computer_move()
        self.assertEqual(self.game.board.count_pieces(), 1)

    def test_game_over(self):
        self.assertFalse(self.game.game_over())

        self.game.board.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.game.game_over())

        self.game.board.board = [['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]
        self.assertTrue(self.game.game_over())

        self.game.board.board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertTrue(self.game.game_over())

    def test_restart_game(self):
        self.game.restart_game()
        self.assertEqual(self.game.board.count_pieces(), 0)

    def test_full_game_draw(self):
        self.game.player_move(0, 0)
        self.game.computer_move()
        self.game.player_move(0, 1)
        self.game.computer_move()
        self.game.player_move(0, 2)
        self.game.computer_move()
        self.game.player_move(1, 0)
        self.game.computer_move()
        self.game.player_move(1, 2)
        self.game.computer_move()
        self.game.player_move(1, 1)
        self.game.computer_move()
        self.game.player_move(2, 0)
        self.game.computer_move()
        self.game.player_move(2, 2)
        self.game.computer_move()
        self.game.player_move(2, 1)
        self.assertTrue(self.game.game_over())

    def test_full_game_player_x_win(self):
        self.game.player_move(0, 0)
        self.game.computer_move()
        self.game.player_move(1, 1)
        self.game.computer_move()
        self.game.player_move(0, 1)
        self.game.computer_move()
        self.game.player_move(2, 2)
        self.game.computer_move()
        self.game.player_move(0, 2)
        self.assertTrue(self.game.game_over())

    def test_full_game_player_o_win(self):
        self.game.player_move(0, 0)
        self.game.computer_move()
        self.game.player_move(1, 1)
        self.game.computer_move()
        self.game.player_move(2, 2)
        self.game.computer_move()
        self.game.player_move(0, 1)
        self.game.computer_move()
        self.game.player_move(1, 0)
        self.game.computer_move()
        self.game.player_move(2, 1)
        self.assertTrue(self.game.game_over())


if __name__ == '__main__':
    unittest.main()