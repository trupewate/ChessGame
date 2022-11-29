#defining interface for pieces
from constants import SQUARE_SIZE

class Piece():
    def __init__(self):

        #center of the square
        self.x = 0
        self.y = 0
        self.calculate_pos()
        
    def calculate_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def move(self, row, col, board):
        self.row = row
        self.col = col
    
    def get_valid_moves(self):
        pass

