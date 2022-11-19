#defining interface for pieces
BLACK = "black"
class Piece():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def move():
        pass


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

b1 = Bishop(1, 1, BLACK)
print(b1)
