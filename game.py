from board import Board


class Game:
    def __init__(self):
        """Конструктор класу Game. Ініціалізує дошку та поточного гравця."""
        self.board = Board()
        self.current_player = 'X'

    def player_move(self, row, col):
        """Виконує хід гравця в позиції (row, col). Повертає True, якщо хід успішний, інакше - False."""
        if self.board.is_valid_move(row, col):
            self.board.place_piece(row, col, self.current_player)
            return True
        return False

    def computer_move(self):
        """Виконує хід комп'ютера."""
        for row in range(3):
            for col in range(3):
                if self.board.is_valid_move(row, col):
                    self.board.place_piece(row, col, 'O')
                    return

    def game_over(self):
        """Перевіряє, чи гра завершилась (є переможець або дошка заповнена).
           Повертає True, якщо гра закінчена, інакше - False."""
        return self.board.check_rows() or self.board.check_cols() or self.board.check_diags()

    def restart_game(self):
        """Перезапускає гру (очищує дошку)."""
        self.board = Board()