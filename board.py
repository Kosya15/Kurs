class Board:
    def __init__(self):
        """Конструктор класу Board. Ініціалізує дошку 3x3 з пустими значеннями."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        """Виводить дошку на екран."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        """Перевіряє, чи є хід (row, col) допустимим. Повертає True, якщо хід допустимий, інакше - False."""
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            return True
        return False

    def place_piece(self, row, col, piece):
        """Розміщує грушку (X або O) на дошці в позиції (row, col)."""
        self.board[row][col] = piece

    def check_rows(self):
        """Перевіряє, чи є переможець в рядках. Повертає True, якщо є переможець, інакше - False."""
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        return False

    def check_cols(self):
        """Перевіряє, чи є переможець в стовпцях. Повертає True, якщо є переможець, інакше - False."""
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        return False

    def check_diags(self):
        """Перевіряє, чи є переможець на діагоналях. Повертає True, якщо є переможець, інакше - False."""
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        """Перевіряє, чи заповнена дошка. Повертає True, якщо дошка заповнена, інакше - False."""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def count_pieces(self):
        """Підраховує кількість грушок на дошці. Повертає загальну кількість грушок."""
        count = 0
        for row in self.board:
            for col in row:
                if col != ' ':
                    count += 1
        return count