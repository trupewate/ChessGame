from piece import Piece
from constants import WHITE_BISHOP, BLACK_BISHOP, WHITE

class Bishop(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_BISHOP if self.color == WHITE else BLACK_BISHOP

    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col
    
    def get_valid_moves(self, board):
        row, col = self.row, self.col
        valid_moves = []
        
        row1 = row - 1
        col1 = col - 1
        while row1 >= 0 and col1 >= 0:
            if board[row1][col1] != 0:
                if board[row1][col1].color != self.color:
                    valid_moves.append((row1, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col1))
            row1 -= 1
            col1 -= 1
        
        row1 = row + 1
        col1 = col - 1
        while row1 < 8 and col1 >= 0:
            if board[row1][col1] != 0:
                if board[row1][col1].color != self.color:
                    valid_moves.append((row1, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col1))
            row1 += 1
            col1 -= 1
        
        row1 = row + 1
        col1 = col + 1
        while row1 < 8 and col1 < 8:
            if board[row1][col1] != 0:
                if board[row1][col1].color != self.color:
                    valid_moves.append((row1, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col1))
            row1 += 1
            col1 += 1
        
        row1 = row - 1
        col1 = col + 1
        while row1 >= 0 and col1 < 8:
            if board[row1][col1] != 0:
                if board[row1][col1].color != self.color:
                    valid_moves.append((row1, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col1))
            row1 -= 1
            col1 += 1

        return valid_moves