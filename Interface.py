import pygame

from constants import WIDTH, HEIGHT, GREY, WHITE, SQUARE_SIZE, WHITE_PAWN, WHITE_KNIGHT, WHITE_BISHOP, WHITE_ROOK,WHITE_QUEEN, WHITE_KING, BLACK_PAWN, BLACK_KNIGHT, BLACK_BISHOP,BLACK_ROOK, BLACK_QUEEN, BLACK_KING

FPS = 60
#variables:
selected = None
board = []


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChessLife")
clock = pygame.time.Clock()
def main():

    run = True

    while run:
        clock.tick(FPS)
        drawBoard(window)
        drawInitialPosition(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos
                row, col = get_row_col_from_mouse(pos)
        pygame.display.flip()
    pygame.quit()


def drawBoard(window):
    window.fill(WHITE)
    for row in range(8):
        for col in range(8):
            if row % 2 == (col + 1) % 2:
                pygame.draw.rect(window, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, row*SQUARE_SIZE + SQUARE_SIZE, col*SQUARE_SIZE + SQUARE_SIZE)) 
            else:
                pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, row*SQUARE_SIZE + SQUARE_SIZE, col*SQUARE_SIZE + SQUARE_SIZE))

def drawInitialPosition(window):
    white_pawn = pygame.transform.scale(pygame.image.load("assets/WhitePawn.png"), (80, 95))
    row1, row2 = 6, 1
    for col in range(8):
        window.blit(WHITE_PAWN, (col * SQUARE_SIZE - 1, row1 * SQUARE_SIZE - 10))
        window.blit(BLACK_PAWN, (col * SQUARE_SIZE - 1, row2 * SQUARE_SIZE - 10))
    
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
    
main()
