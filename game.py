import pygame
from constants import WHITE, BLACK, DRAW
from board import Board
from Pieces import pawn, knight, bishop, rook, queen, king
import copy

class Game():
    def __init__(self):
        self.previous_move = 0
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.all_white_valid_moves = []
        self.all_black_valid_moves = []
        self.create_all_valid_moves()
        self.is_check = False
        self.is_mate = False
        self.is_stalemate = False
        self.attacking_piece = []
        self.winner = None

    def create_all_valid_moves(self):
        self.all_white_valid_moves.clear()
        self.all_black_valid_moves.clear()
        for piece in self.board.white_pieces:
            self.all_white_valid_moves.extend(piece.get_valid_moves(self))
        for piece in self.board.black_pieces:
            self.all_black_valid_moves.extend(piece.get_valid_moves(self))
        #print(self.all_white_valid_moves)

    def select(self, row, col):
        if (self.selected != None) and ((row, col) in self.valid_moves):
            self.move(row, col, self.selected)
            self.selected = None
            self.valid_moves.clear()
        else:
            self.valid_moves.clear()
            piece = self.board.board[row][col]
            if self.turn == WHITE:
                self.is_check = self.board.white_king.is_check(self)
            else:
                self.is_check = self.board.black_king.is_check(self)
            #print(self.is_check)
            if self.is_check:
                if piece != 0 and piece.color == self.turn:
                    #only king can move if not mate
                    if type(piece) == king.King:
                        self.selected = piece
                        self.valid_moves = piece.get_valid_moves(self)
                        self.check_pin(piece)
                    #piece can block or capture the checking piece
                    else:
                        self.selected = piece
                        self.block_from_check_or_capture(piece)
                        self.check_pin(piece)
                else:
                    self.selected = None
                    
            else:
                if piece != 0 and piece.color == self.turn and type(piece) == king.King:
                    if piece.color == WHITE:
                        self.selected = piece
                        self.valid_moves = piece.get_valid_moves(self) + piece.castle(self)
                        print(piece.castle(self))
                    else:
                        self.selected = piece
                        self.valid_moves = piece.get_valid_moves(self) + piece.castle(self)
                        print(self.valid_moves)
                        
                        
                else:
                    if piece != 0 and piece.color == self.turn:
                        self.selected = piece
                        self.valid_moves = piece.get_valid_moves(self)
                        self.check_pin(piece)
    def checkmate(self):
        if self.turn == WHITE:
            self.is_check = self.board.white_king.is_check(self)
        else:
            self.is_check = self.board.black_king.is_check(self)
        actual_valid_moves = []
        if self.turn == WHITE:
            if self.is_check:
                for piece in self.board.white_pieces:
                    self.valid_moves = piece.get_valid_moves(self)
                    if type(piece) == king.King:
                        self.check_pin(piece)
                    else:
                        self.block_from_check_or_capture(piece)
                    actual_valid_moves.extend(self.valid_moves)
                print(actual_valid_moves)
                if len(actual_valid_moves) == 0:
                    self.is_mate = True
                    self.winner = BLACK
        else:
            if self.is_check:
                for piece in self.board.black_pieces:
                    self.valid_moves = piece.get_valid_moves(self)
                    if type(piece) == king.King:
                        self.check_pin(piece) 
                    else:
                        self.block_from_check_or_capture(piece)
                    actual_valid_moves.extend(self.valid_moves)
                print(actual_valid_moves)
                if len(actual_valid_moves) == 0:
                    self.is_mate = True
                    self.winner = WHITE
    
    def stalemate(self):
        if self.turn == WHITE:
            self.is_check = self.board.white_king.is_check(self)
        else:
            self.is_check = self.board.black_king.is_check(self)
        actual_valid_moves = []
        if self.turn == WHITE:
            if not self.is_check:
                for piece in self.board.white_pieces:
                    self.valid_moves = piece.get_valid_moves(self)
                    self.check_pin(piece)
                    actual_valid_moves.extend(self.valid_moves)
                if len(actual_valid_moves) == 0:
                    self.is_stalemate = True
                    self.winner = DRAW
        else:
            if not self.is_check:
                print(self.board.black_pieces)
                for piece in self.board.black_pieces:
                    self.valid_moves = piece.get_valid_moves(self)
                    self.check_pin(piece)
                    actual_valid_moves.extend(self.valid_moves)
                if len(actual_valid_moves) == 0:
                    self.is_stalemate = True
                    self.winner = DRAW
                    

    def move(self, row, col, piece):
        old_row, old_col = piece.get_position()
        self.selected.move(row, col, self.board.board)
        if type(self.selected) == king.King or type(self.selected) == rook.Rook:
            self.selected.moved = True
        piece2 = self.board.board[row][col]
        if self.previous_move != 0:
            piece3, r1, c1, r2, c2 = self.previous_move
        #check if capture
        if piece2 != 0:
            if self.turn == BLACK:
                self.board.white_pieces.remove(piece2)
            else:
                self.board.black_pieces.remove(piece2)
        #check if capture by un passant and promotion
        if type(piece) == pawn.Pawn:
            if old_col != col and piece2 == 0:
                if self.turn == BLACK:
                    if old_col - col == 1:
                        self.board.white_pieces.remove(piece3)
                        self.board.board[old_row][col] = 0
                    elif old_col - col == - 1:
                        self.board.white_pieces.remove(piece3)
                        self.board.board[old_row][col] = 0
                else:
                    if old_col - col == 1:
                        self.board.black_pieces.remove(piece3)
                        self.board.board[old_row][col] = 0
                    elif old_col - col == - 1:
                        self.board.black_pieces.remove(piece3)
                        self.board.board[old_row][col] = 0

        self.board.board[row][col] = piece
        self.board.board[old_row][old_col] = 0 
        self.previous_move = (piece, old_row, old_col, row, col)
        self.promote(piece, row, col)
        self.turn = BLACK if piece.color == WHITE else WHITE
        
        #update all valid moves for white pieces
        self.create_all_valid_moves()
        #print(self.all_white_valid_moves)
        #print(self.board.white_pieces)

        #checkmate and stalemate check
        self.stalemate()
        self.checkmate()

    def promote(self, piece, row, col):
        if type(piece) == pawn.Pawn:
            if self.turn == WHITE:
                if row == 0:
                    self.board.board[row][col] = 0
                    self.board.white_pieces.remove(piece)
                    self.board.board[row][col] = queen.Queen(row, col, WHITE)
                    self.board.white_pieces.append(self.board.board[row][col])
            else:
                if row == 8:
                    self.board.board[row][col] = 0
                    self.board.black_pieces.remove(piece)
                    self.board.board[row][col] = queen.Queen(row, col, BLACK)
                    self.board.black_pieces.append(self.board.board[row][col])

    
    def block_from_check_or_capture(self, piece):
        self.valid_moves.clear()
        potenial_valid_moves = piece.get_valid_moves(self)
        squares_between_king_and_attacking_piece = []
        self.attacking_piece = []
        #finding position of the King
        if self.turn == WHITE:
            king_row, king_col = self.board.white_king.row, self.board.white_king.col
        else:
            king_row, king_col = self.board.black_king.row, self.board.black_king.col
        #finding the piece attacking king
        if self.turn == WHITE:
            for p in self.board.black_pieces:
                moves = p.get_valid_moves(self)
                if (king_row, king_col) in moves:
                    self.attacking_piece.append(p)
        else:
            for p in self.board.white_pieces:
                moves = p.get_valid_moves(self)
                if (king_row, king_col) in moves:
                    self.attacking_piece.append(p)

        #finding squares between King and the attacking pieces
        #print(self.attacking_piece)
        if len(self.attacking_piece) == 2:
            self.valid_moves = []
        elif len(self.attacking_piece) == 1:
            attacking_row, attacking_col = self.attacking_piece[0].row, self.attacking_piece[0].col
            if type(self.attacking_piece[0]) == knight.Knight:
                if (attacking_row, attacking_col) in potenial_valid_moves:
                    self.valid_moves.append((attacking_row, attacking_col))
            else:
                #finding squares between king and attacking piece via vertical, horizontal and diagonal checks
                min_row = min(king_row, attacking_row)
                min_col = min(king_col, attacking_col)
                max_row = max(king_row, attacking_row)
                max_col = max(king_col, attacking_col)
                for i in range(max(max_row - min_row, max_col - min_col) + 1):
                    if min_row == max_row:
                        squares_between_king_and_attacking_piece.append((min_row, min_col + i))
                    elif min_col == max_col:
                        squares_between_king_and_attacking_piece.append((min_row + i, min_col))
                    else:
                        if (max_row == king_row and max_col == king_col) or (max_row == attacking_row and max_col == attacking_col):
                            squares_between_king_and_attacking_piece.append((min_row + i, min_col + i))
                        else:
                            squares_between_king_and_attacking_piece.append((max_row - i, min_col + i))
                #print(squares_between_king_and_attacking_piece)
            #checking for the moves in squares_between_king_and_attacking_piece
                for move in potenial_valid_moves:
                    if move in squares_between_king_and_attacking_piece:
                        self.valid_moves.append(move)
            
            
    def find_squares():
        pass
    
    def check_pin(self, piece):
        #get valid moves
        #check if after each move it is check to the side whose move it was
        #if it is check remove that move from valid moves
        old_row, old_col = piece.get_position()
        valid_moves = piece.get_valid_moves(self)
        self.valid_moves = piece.get_valid_moves(self)
        #print(valid_moves)
        for row, col in valid_moves:
    
            piece.move(row, col, self.board.board)
            piece2 = self.board.board[row][col]
            if piece2 != 0:
                if self.turn == BLACK:
                    self.board.white_pieces.remove(piece2)
                else:
                    self.board.black_pieces.remove(piece2)
            self.board.board[row][col] = piece
            self.board.board[old_row][old_col] = 0
            self.create_all_valid_moves()
            
            #check if check
            if self.turn == WHITE:
                if self.board.white_king.is_check(self):
                    #print("remove")
                    self.valid_moves.remove((row, col))
            else:
                if self.board.black_king.is_check(self):
                    self.valid_moves.remove((row, col))
            #return piece to original positions
            self.board.board[row][col] = piece2
            self.board.board[old_row][old_col] = piece
            piece.move(old_row, old_col, self.board.board)
            if piece2 != 0:
                if self.turn == BLACK:
                    self.board.white_pieces.append(piece2)
                else:
                    self.board.black_pieces.append(piece2)
            self.create_all_valid_moves()
            


            


        

    
