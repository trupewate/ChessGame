import pygame
from constants import WHITE, BLACK
from board import Board
from Pieces import pawn, knight, bishop, rook, queen, king

class Game():
    def __init__(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.all_white_valid_moves = []
        self.all_black_valid_moves = []
        self.create_all_valid_moves()
        self.is_check = False
    def create_all_valid_moves(self):
        for piece in self.board.white_pieces:
            self.all_white_valid_moves.extend(piece.get_valid_moves(self.board))
        for piece in self.board.black_pieces:
            self.all_black_valid_moves.extend(piece.get_valid_moves(self.board))
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
            print(self.is_check)
            if self.is_check:
                #only king can move if not mate
                if type(piece) == king.King:
                    self.selected = piece
                    self.valid_moves = piece.get_valid_moves(self.board)
            else:
                if piece != 0 and piece.color == self.turn:
                    self.selected = piece
                    self.valid_moves = piece.get_valid_moves(self.board)
    def move(self, row, col, piece):
        old_row, old_col = piece.get_position()
        self.selected.move(row, col)
        self.board.board[row][col] = piece
        self.board.board[old_row][old_col] = 0 
        self.turn = BLACK if piece.color == WHITE else WHITE
        
        #update all valid moves for white pieces
        self.all_white_valid_moves.clear()
        self.all_black_valid_moves.clear()
        self.create_all_valid_moves()
        #print(self.all_white_valid_moves)
        #print(self.board.white_pieces)
        for piece in self.board.white_pieces:
            print((piece.row, piece.col))
        

    
