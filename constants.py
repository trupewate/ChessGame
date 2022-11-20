import pygame

WIDTH = 640
HEIGHT = 640
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // ROWS


#colors
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#pieces
WHITE_PAWN = pygame.transform.scale(pygame.image.load("assets/WhitePawn.png"), (80, 85))
BLACK_PAWN = pygame.transform.scale(pygame.image.load("assets/BlackPawn.png"), (80, 85))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load("assets/WhiteKnight.png"), (80, 85))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load("assets/BlackKnight.png"), (80, 85))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load("assets/WhiteBishop.png"), (80, 85))
BLACK_BISHOP= pygame.transform.scale(pygame.image.load("assets/BlackBishop.png"), (80, 85))
WHITE_ROOK = pygame.transform.scale(pygame.image.load("assets/WhiteRook.png"), (80, 85))
BLACK_ROOK = pygame.transform.scale(pygame.image.load("assets/BlackRook.png"), (80, 85))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load("assets/WhiteQueen.png"), (80, 85))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load("assets/BlackQueen.png"), (80, 85))
WHITE_KING = pygame.transform.scale(pygame.image.load("assets/WhiteKing.png"), (80, 85))
BLACK_KING = pygame.transform.scale(pygame.image.load("assets/BlackKing.png"), (80, 85))
