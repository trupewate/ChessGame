from piece import Piece
from constants import WHITE_PAWN, BLACK_PAWN, WHITE, BLACK

class Pawn(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_PAWN if self.color == WHITE else BLACK_PAWN
        self.promote = None
    
    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.row, self.col
        if self.color == WHITE:
            if row - 1 >= 0 and col - 1 >= 0:
                left_piece = board.board[row - 1][col - 1]
            else:
                left_piece = 0
            if col + 1 < 8 and row - 1 >= 0:
                right_piece = board.board[row - 1][col + 1]
            else:
                right_piece = 0
            #promotion
            if row == 0:
                #user choice
                pass
            #un passant
            #if row == 3 and previous.move == row 2 - row 4 nearby

            if row == 6:
                if board.board[row- 1][col] == 0:
                    valid_moves.append((row - 1, col))
                if board.board[row - 2][col] == 0:
                    valid_moves.append((row - 2, col))
            elif board.board[row - 1][col] == 0:
                valid_moves.append((row - 1, col))
            if left_piece != 0:
                if left_piece.color != self.color:
                    valid_moves.append((row - 1, col - 1))
            if right_piece != 0:
                if right_piece.color != self.color:
                    valid_moves.append((row - 1, col + 1))

        else:
            if row + 1 < 8 and col + 1 < 8:
                right_piece = board.board[row + 1][col + 1]
            else:
                right_piece = 0
            if col - 1 >= 0 and row + 1 < 8:
                left_piece = board.board[row + 1][col - 1]
            else:
                left_piece = 0
            #promotion
            if row == 8:
                #user choice
                pass
            #un passant
            #if row == 3 and previous.move == row 2 - row 4 nearby

            if row == 1:
                if board.board[row + 1][col] == 0:
                    valid_moves.append((row + 1, col))
                if board.board[row + 2][col] == 0:
                    valid_moves.append((row + 2, col))
            elif board.board[row + 1][col] == 0:
                valid_moves.append((row + 1, col))
            if left_piece != 0:
                if left_piece.color != self.color:
                    valid_moves.append((row + 1, col - 1))
            if right_piece != 0:
                if right_piece.color != self.color:
                    valid_moves.append((row + 1, col + 1))
        return valid_moves