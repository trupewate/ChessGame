from piece import Piece
from constants import WHITE_KNIGHT, BLACK_KNIGHT, WHITE, ROWS, COLS

class Knight(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_KNIGHT if self.color == WHITE else BLACK_KNIGHT

    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col
    
    def get_valid_moves(self, board):
        row, col = self.row, self.col
        #move1
        valid_moves = []
        coordinates = [(row + 2, col + 1), (row + 2, col -1), (row - 2, col + 1), (row - 2, col - 1), (row + 1, col + 2),(row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]
        for x, y in coordinates:
            if 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 0:
                    valid_moves.append((x, y))
                elif board[x][y].color != self.color:
                    valid_moves.append((x, y))

        return valid_moves