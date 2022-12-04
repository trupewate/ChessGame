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
        self.white_castled = False
        self.black_castled = False    
    def get_type(self):
        return self.type

    def get_position(self):
        return self.row, self.col

    def move(self, row, col, board):
        if self.color == WHITE:
            if col - self.col == 2:
                #short castle
                rook1 = board[7][7]
                rook1.move(7, 5, board)
                board[7][5] = rook1
                board[7][7] = 0
                self.white_castled = True
            elif self.col - col == 2:
                #long castle
                rook2 = board[7][0]
                rook2.move(7, 3, board)
                board[7][3] = rook2
                board[7][0] = 0
                self.white_castled = True
        else:
            if col - self.col == 2:
                #short castle
                rook1 = board[0][7]
                rook1.move(0, 5, board)
                board[0][5] = rook1
                board[0][7] = 0
                self.black_castled = True
            elif self.col - col == 2:
                #print()
                #long castle
                rook2 = board[0][0]
                rook2.move(0, 3, board)
                board[0][3] = rook2
                board[0][0] = 0
                self.black_castled = True
            
        self.row = row
        self.col = col

    

    def is_check(self, game):
        if self.color == WHITE:
            if (self.row, self.col) in game.all_black_valid_moves:
                return True
        else:
            if (self.row, self.col) in game.all_white_valid_moves:
                return True
        return False

     
    def castle(self, game):  
        
        board = game.board
        valid_moves = []
        row, col = self.get_position()
        c1 = [(row, col + 1), (row, col + 2)]
        c2 = [(row, col - 1), (row, col - 2)]
        c3 = [(0, col + 1), (0, col + 2)]
        c4 = [(0, col - 1), (0, col - 2)]

        rook1 = board.board[7][7]
        rook2 = board.board[7][0]
        rook3 = board.board[0][7]
        rook4 = board.board[0][0]


        if not self.moved:
            if self.color == WHITE:
                if board.board[row][col + 1] == 0 and board.board[row][col + 2] == 0 and all(coordinate not in game.all_black_valid_moves for coordinate in c1) and rook1 != 0 and type(rook1) == rook.Rook and not rook1.moved:
                    valid_moves.append((7, 6))
                elif board.board[row][col - 1] == 0 and board.board[row][col - 2] == 0 and board.board[row][col - 3] == 0 and all(coordinate not in game.all_black_valid_moves for coordinate in c2) and rook2 != 0 and type(rook2) == rook.Rook and not rook2.moved:
                    valid_moves.append((7, 2))
            else:
                if board.board[0][col + 1] == 0 and board.board[0][col + 2] == 0 and all(coordinate not in game.all_white_valid_moves for coordinate in c3) and rook3 != 0 and type(rook3) == rook.Rook and not rook3.moved:
                    valid_moves.append((0, 6))
                elif board.board[0][col -1] == 0 and board.board[0][col -2] == 0 and board.board[0][col - 3] == 0 and all(coordinate not in game.all_white_valid_moves for coordinate in c4) and rook4 != 0 and type(rook4) == rook.Rook and not rook4.moved:
                    valid_moves.append((0, 2))
        
        return valid_moves

    def get_valid_moves(self, game):
        # i need to delete the moves which are blocked by other
        
        board = game.board
        row, col = self.row, self.col
        potential_moves = [(row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row + 1, col), (row -1, col + 1), (row -1, col - 1), (row -1, col)]
        potential_moves_copy = [(row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row + 1, col), (row -1, col + 1), (row -1, col - 1), (row -1, col)]
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
            elif type(piece) == King:
                row, col = piece.row, piece.col
                blocked_squares.extend(((row, col + 1), (row, col - 1), (row + 1, col + 1), (row + 1, col - 1), (row + 1, col), (row -1, col + 1), (row -1, col - 1), (row -1, col )))
            else:
                blocked_squares.extend(piece.get_valid_moves(game))
            
        
        for i in range(len(potential_moves)):
            if potential_moves[i] not in blocked_squares:
                valid_moves.append(potential_moves[i])
    

        return valid_moves