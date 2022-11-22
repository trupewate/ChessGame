from piece import Piece
from constants import WHITE_KING, BLACK_KING, WHITE

class King(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_KING if self.color == WHITE else BLACK_KING
    
    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col
    
    def get_valid_moves(self, board):
        row, col = self.row, self.col
        