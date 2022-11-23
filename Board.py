
from Pieces.pawn import Pawn
from Pieces.knight import Knight
from Pieces.bishop import Bishop
from Pieces.rook import Rook
from Pieces.queen import Queen
from Pieces.king import King
from constants import ROWS, COLS, BLACK, WHITE
class Board():
    def __init__(self):
        self.board = []
        self.white_pieces = []
        self.black_pieces = []
        self.white_king = None
        self.black_king = None
        self.createBoard()
        

    def createBoard(self):
        for i in range(ROWS):
            self.board.append([])
        #filling with 0's all squares in the board representing empty spaces
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row].append(0)
        #filling the board with pieces
        
        #pawns
        for col in range(COLS):
            row1, row2 = 1, 6
            piece1, piece2 = Pawn(row1, col, BLACK), Pawn(row2, col, WHITE)
            self.board[row1][col] = piece1 
            self.board[row2][col] = piece2
            self.white_pieces.append(piece2)
            self.black_pieces.append(piece1)   
        
        #Rooks
        for col in range(0, 8, 7):
            row1, row2 = 0, 7
            piece1, piece2 = Rook(row1, col, BLACK), Rook(row2, col, WHITE)
            self.board[row1][col] = piece1 
            self.board[row2][col] = piece2
            self.white_pieces.append(piece2)
            self.black_pieces.append(piece1)
        
        #Knights
        for col in range(1, 7, 5):
            row1, row2 = 0, 7
            piece1, piece2 = Knight(row1, col, BLACK), Knight(row2, col, WHITE)
            self.board[row1][col] = piece1 
            self.board[row2][col] = piece2
            self.white_pieces.append(piece2)
            self.black_pieces.append(piece1) 
        
        #Bishops
        for col in range(2, 6, 3):
            row1, row2 = 0, 7
            piece1, piece2 = Bishop(row1, col, BLACK), Bishop(row2, col, WHITE)
            self.board[row1][col] = piece1 
            self.board[row2][col] = piece2
            self.white_pieces.append(piece2)
            self.black_pieces.append(piece1) 
        
        #Queens
        row1, row2 = 0, 7
        col = 3
        piece1, piece2 = Queen(row1, col, BLACK), Queen(row2, col, WHITE)
        self.board[row1][col] = piece1 
        self.board[row2][col] = piece2
        self.white_pieces.append(piece2)
        self.black_pieces.append(piece1)

        #Kings
        row1, row2 = 0, 7
        col = 4
        piece1, piece2 = King(row1, col, BLACK), King(row2, col, WHITE)
        self.board[row1][col] = piece1 
        self.board[row2][col] = piece2
        self.white_pieces.append(piece2)
        self.black_pieces.append(piece1)
        self.white_king = self.board[row2][col]
        self.black_king = self.board[row1][col]
        