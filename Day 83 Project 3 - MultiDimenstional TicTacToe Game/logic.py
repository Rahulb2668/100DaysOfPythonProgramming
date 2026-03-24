import numpy as np


class Board:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)

    def is_valid_move(self, row, column):
        return self.board[row, column] == 0

    def place_mark(self, row, column, player_id):  # Added player_id here
        if self.is_valid_move(row, column):
            self.board[row, column] = player_id
            return True
        return False

    def is_draw(self):
        return not np.any(self.board == 0)

    def check_win(self, player_id):
        for r in range(3):
            if np.all(self.board[r, :] == player_id):
                return True
        for c in range(3):
            if np.all(self.board[:, c] == player_id):
                return True

        if np.all(np.diag(self.board) == player_id):
            return True

        if np.all(np.diag(np.fliplr(self.board)) == player_id):
            return True

        return False