import pygame

from constants import WIDTH, HEIGHT, GREY, WHITE, SQUARE_SIZE, WHITE_PAWN, WHITE_KNIGHT, WHITE_BISHOP, WHITE_ROOK,WHITE_QUEEN, WHITE_KING, BLACK_PAWN, BLACK_KNIGHT, BLACK_BISHOP,BLACK_ROOK, BLACK_QUEEN, BLACK_KING
import Pieces


def calculate_pos(row, col):
    x = SQUARE_SIZE * col + SQUARE_SIZE // 2
    y = SQUARE_SIZE * row + SQUARE_SIZE // 2
    return x, y

def drawPiece(window, piece, row, col):
    x, y = calculate_pos(row, col)
    window.blit(piece, (x - piece.get_width() / 2 - 1, y - piece.get_height() / 2))
    

def drawBoard(window):
    window.fill(WHITE)
    for row in range(8):
        for col in range(8):
            if row % 2 == (col + 1) % 2:
                pygame.draw.rect(window, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, row*SQUARE_SIZE + SQUARE_SIZE, col*SQUARE_SIZE + SQUARE_SIZE)) 
            else:
                pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, row*SQUARE_SIZE + SQUARE_SIZE, col*SQUARE_SIZE + SQUARE_SIZE))

def drawInitialPosition(window):
    row1, row2 = 6, 1
    for col in range(8):
        drawPiece(window, WHITE_PAWN, row1, col)
        drawPiece(window, BLACK_PAWN, row2, col)
    
    row1, row2 = 0, 7
    for col in range(0, 8, 7):
        window.blit(WHITE_ROOK, (col * SQUARE_SIZE - 1, row2 * SQUARE_SIZE - 10))
        window.blit(BLACK_ROOK, (col * SQUARE_SIZE - 1, row1 * SQUARE_SIZE - 10))

    row1, row2 = 0, 7
    for col in range(1, 8, 5):
        window.blit(WHITE_KNIGHT, (col * SQUARE_SIZE - 1, row2 * SQUARE_SIZE - 10))
        window.blit(BLACK_KNIGHT, (col * SQUARE_SIZE - 1, row1 * SQUARE_SIZE - 10))

    row1, row2 = 0, 7
    for col in range(2, 6, 3):
        window.blit(WHITE_BISHOP, (col * SQUARE_SIZE - 1, row2 * SQUARE_SIZE - 10))
        window.blit(BLACK_BISHOP, (col * SQUARE_SIZE - 1, row1 * SQUARE_SIZE - 10))

    row1, row2 = 0, 7
    col = 3
    window.blit(WHITE_QUEEN, (col * SQUARE_SIZE - 1, row2 * SQUARE_SIZE - 10))
    window.blit(BLACK_QUEEN, (col * SQUARE_SIZE - 1, row1 * SQUARE_SIZE - 10))

    row1, row2 = 0, 7
    col = 4
    window.blit(WHITE_KING, (col * SQUARE_SIZE - 1, row2 * SQUARE_SIZE - 10))
    window.blit(BLACK_KING, (col * SQUARE_SIZE - 1, row1 * SQUARE_SIZE - 10))

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def move(window):
    pass
def select(row, col):
    pass
def createboard():
    pass
    
