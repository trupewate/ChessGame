from piece import Piece
from Pieces import pawn, rook
from constants import WHITE_KING, BLACK_KING, WHITE

class King(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col
        self.type = WHITE_KING if self.color == WHITE else BLACK_KING
        self.moved = False
    
    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col

    def move(self, row, col):
        self.row = row
        self.col = col
        self.moved = True

    

    def is_check(self, game):
        if self.color == WHITE:
            print()
            if (self.row, self.col) in game.all_black_valid_moves:
                return True
        else:
            if (self.row, self.col) in game.all_white_valid_moves:
                return True
        return False

    def castle(self, game):
        board = game.board.board
        valid_moves = []
        row, col = self.get_position()
        rook1 = board.board[7][7]
        rook2 = board.board[7][0]

        if not self.moved:
            if board.board[row][col + 1] == 0 and board.board[row][col + 2] == 0 and rook1 != 0 and type(rook1) == rook.Rook and not rook1.moved:
                if self.color == WHITE:
                    if board.board[row][col + 1] not in board.
    def get_valid_moves(self, board):
        row, col = self.row, self.col
        potential_moves = [(row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row + 1, col), (row -1, col + 1), (row -1, col - 1), (row -1, col )]
        potential_moves_copy = [(row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row + 1, col), (row -1, col + 1), (row -1, col - 1), (row -1, col )]
        #checking for nearby own pieces:

        for i in range(len(potential_moves_copy)):
            row1, col1 = potential_moves_copy[i]
            if (0 <= row1 < 8) and (0 <= col1 < 8):
                if board.board[row1][col1] != 0:
                    if board.board[row1][col1].color == self.color:
                        potential_moves.remove((row1, col1))
            else:
                potential_moves.remove((row1, col1))

        blocked_squares = []
        valid_moves = []
        if self.color == WHITE:
            pieces = board.black_pieces
        else:
            pieces = board.white_pieces
        for piece in pieces:
            if type(piece) == pawn.Pawn:
                r, c = piece.row, piece.col
                if piece.color == WHITE:
                    blocked_squares.extend(((r - 1, c - 1), (r - 1, c + 1)))
                else:
                    blocked_squares.extend(((r + 1, c + 1), (r + 1, c - 1)))
            elif type(piece) != King:
                blocked_squares.extend(piece.get_valid_moves(board))
            else:
                row, col = piece.row, piece.col
        blocked_squares.extend(((row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row + 1, col), (row -1, col + 1), (row -1, col - 1), (row -1, col )))
        for i in range(len(potential_moves)):
            if potential_moves[i] not in blocked_squares:
                valid_moves.append(potential_moves[i])
        
        #castling
        row, col = self.get_position()
        rook1 = board.board[7][7]
        rook2 = board.board[7][0]

        if not self.moved:
            if board.board[row][col + 1] == 0 and board.board[row][col + 2] == 0 and rook1 != 0 and type(rook1) == rook.Rook and not rook1.moved:
                if self.color == WHITE:
                    if board.board[row][col + 1] not in board.
        return valid_moves