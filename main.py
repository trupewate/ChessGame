import pygame
from Interface import drawBoard, drawInitialPosition, get_row_col_from_mouse
from constants import WIDTH, HEIGHT
FPS = 60
#variables:


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

main()