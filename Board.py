
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
            self.board[row1][col] = Pawn(row1, col, BLACK) 
            self.board[row2][col] = Pawn(row2, col, WHITE)   
        
        #Rooks
        for col in range(0, 8, 7):
            row1, row2 = 0, 7
            self.board[row1][col] = Rook(row1, col, BLACK)
            self.board[row2][col] = Rook(row2, col, WHITE)
        
        #Knights
        for col in range(1, 7, 5):
            row1, row2 = 0, 7
            self.board[row1][col] = Knight(row1, col, BLACK)
            self.board[row2][col] = Knight(row2, col, WHITE)
        
        #Bishops
        for col in range(2, 6, 3):
            row1, row2 = 0, 7
            self.board[row1][col] = Bishop(row1, col, BLACK)
            self.board[row2][col] = Bishop(row2, col, WHITE)
        
        #Queens
        row1, row2 = 0, 7
        col = 3
        self.board[row1][col] = Queen(row1, col, BLACK)
        self.board[row2][col] = Queen(row2, col, WHITE)

        #Kings
        row1, row2 = 0, 7
        col = 4
        self.board[row1][col] = King(row1, col, BLACK)
        self.board[row2][col] = King(row2, col, WHITE)
        