#defining interface for pieces
from constants import SQUARE_SIZE

class Piece():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.promote = None

        #center of the square
        self.x = 0
        self.y = 0
        
    def calculate_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def move(self, row, col):
        self.row = row
        self.col = col


class Bishop(Piece):
    pass



class Pawn(Piece):
    pass
class Knight(Piece):
    pass
class Queen(Piece):
    pass

class King(Piece):
    pass

class Rook(Piece):
    pass

