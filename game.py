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
    
    def select(self, row, col):
        if (self.selected != None) and ((row, col) in self.valid_moves):
            self.move(row, col, self.selected)
            self.selected.move(row, col)
            self.selected = None
            self.valid_moves.clear()
        else:
            self.valid_moves.clear()
            piece = self.board.board[row][col]
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                if type(piece) == pawn.Pawn:
                    self.valid_moves = piece.get_valid_moves(self.board.board)
                elif type(piece) == knight.Knight:
                    self.valid_moves = piece.get_valid_moves(self.board.board)
                elif type(piece) == bishop.Bishop:
                    self.valid_moves = piece.get_valid_moves(self.board.board)
                elif type(piece) == rook.Rook:
                    self.valid_moves = piece.get_valid_moves(self.board.board)
                elif type(piece) == queen.Queen:
                    self.valid_moves = piece.get_valid_moves(self.board.board)
    def move(self, row, col, piece):
        old_row, old_col = piece.get_position() 
        self.board.board[row][col] = piece
        self.board.board[old_row][old_col] = 0 
        self.turn = BLACK if piece.color == WHITE else WHITE
        

    
