from piece import Piece
from constants import WHITE_QUEEN, BLACK_QUEEN, WHITE

class Queen(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_QUEEN if self.color == WHITE else BLACK_QUEEN
    
    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col
    
    def get_valid_moves(self, game):
        board = game.board
        row, col = self.row, self.col
        valid_moves = []
        
        row1 = row + 1
        while row1 < 8:
            if board.board[row1][col] != 0:
                if board.board[row1][col].color != self.color:
                    valid_moves.append((row1, col))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col))
            row1 += 1

        row1 = row - 1
        while row1 >= 0:
            if board.board[row1][col] != 0:
                if board.board[row1][col].color != self.color:
                    valid_moves.append((row1, col))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col))
            row1 -= 1

        col1 = col + 1
        while col1 < 8:
            if board.board[row][col1] != 0:
                if board.board[row][col1].color != self.color:
                    valid_moves.append((row, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row, col1))
            col1 += 1

        col1 = col - 1
        while col1 >= 0:
            if board.board[row][col1] != 0:
                if board.board[row][col1].color != self.color:
                    valid_moves.append((row, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row, col1))
            col1 -= 1

        row1 = row - 1
        col1 = col - 1
        while row1 >= 0 and col1 >= 0:
            if board.board[row1][col1] != 0:
                if board.board[row1][col1].color != self.color:
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
            if board.board[row1][col1] != 0:
                if board.board[row1][col1].color != self.color:
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
            if board.board[row1][col1] != 0:
                if board.board[row1][col1].color != self.color:
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
            if board.board[row1][col1] != 0:
                if board.board[row1][col1].color != self.color:
                    valid_moves.append((row1, col1))
                    break
                else:
                    break
            else:
                valid_moves.append((row1, col1))
            row1 -= 1
            col1 += 1
        return valid_moves