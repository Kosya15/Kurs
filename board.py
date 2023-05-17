class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            return True
        return False

    def place_piece(self, row, col, piece):
        self.board[row][col] = piece

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        return False

    def check_cols(self):
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        return False

    def check_diags(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def count_pieces(self):
        count = 0
        for row in self.board:
            for col in row:
                if col != ' ':
                    count += 1
        return count