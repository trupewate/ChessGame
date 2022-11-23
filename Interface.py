import pygame

from constants import *
import piece
from board import Board
from game import Game
from Pieces.pawn import Pawn

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChessLife")
clock = pygame.time.Clock()

#initialising board
game = Game()


def game_loop():

    run = True

    while run:
        clock.tick(FPS)
        draw_board()
        draw_pieces()
        draw_valid_moves_circles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        pygame.display.flip()
    pygame.quit()

def calculate_pos(row, col):
    x = SQUARE_SIZE * col + SQUARE_SIZE // 2
    y = SQUARE_SIZE * row + SQUARE_SIZE // 2
    return x, y

def drawPiece(piece, row, col):
    x, y = calculate_pos(row, col)
    window.blit(piece, (x - piece.get_width() / 2 - 1, y - piece.get_height() / 2))
    

def draw_board():
    window.fill(WHITE)
    for row in range(8):
        for col in range(8):
            if row % 2 == (col + 1) % 2:
                pygame.draw.rect(window, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, row*SQUARE_SIZE + SQUARE_SIZE, col*SQUARE_SIZE + SQUARE_SIZE)) 
            else:
                pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, row*SQUARE_SIZE + SQUARE_SIZE, col*SQUARE_SIZE + SQUARE_SIZE))

def draw_pieces():
    for i in range(ROWS):
        for j in range(COLS):
                        
            piece = game.board.board[i][j]
            if piece != 0:
                type = piece.get_type()
                x, y = calculate_pos(i, j)
                window.blit(piece.get_type(), (x - type.get_width() / 2 - 1, y - type.get_height() / 2))

def draw_valid_moves_circles():
    valid_moves = game.valid_moves
    for row, col in valid_moves:
        x, y = calculate_pos(row, col)
        pygame.draw.circle(window, BLUE, (x, y), 8)

def get_row_col_from_mouse(pos):

    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


    