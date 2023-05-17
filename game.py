from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def player_move(self, row, col):
        if self.board.is_valid_move(row, col):
            self.board.place_piece(row, col, self.current_player)
            return True
        return False

    def computer_move(self):
        for row in range(3):
            for col in range(3):
                if self.board.is_valid_move(row, col):
                    self.board.place_piece(row, col, 'O')
                    return

    def game_over(self):
        return self.board.check_rows() or self.board.check_cols() or self.board.check_diags()

    def restart_game(self):
        self.board = Board()