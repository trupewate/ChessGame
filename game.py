import pygame
from constants import WHITE
from Board import Board

class Game():
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
