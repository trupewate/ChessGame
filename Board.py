
from Pieces import Bishop, Knight, Pawn, Rook, Queen, King
from constants import ROWS, COLS, WHITE_PIECE, BLACK_PIECE
class Board():
    def __init__(self):
        self.board = []


    def initialPosition(self):
        for i in range(ROWS):
            self.board.append([])
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row].append(0)
        for col in range(COLS):
            row1, row2 = 1, 6
            self.board[row1][col] = Pawn(row1, col, WHITE_PIECE) 
            self.board[row2][col] = Pawn(row2, col, BLACK_PIECE)   
        
