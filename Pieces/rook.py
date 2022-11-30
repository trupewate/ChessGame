from piece import Piece
from constants import WHITE_ROOK, BLACK_ROOK, WHITE

class Rook(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_ROOK if self.color == WHITE else BLACK_ROOK
        self.moved = False

    def get_type(self):
        return self.type

    def move(self, row, col, board):
        self.row = row
        self.col = col
        self.moved = True

    def get_position(self):
        return self.row, self.col

    def get_valid_moves(self, game):
        board = game.board
        valid_moves = []
        row, col = self.row, self.col
        
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
        
        return valid_moves