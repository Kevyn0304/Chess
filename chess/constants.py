import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//ROWS

#rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
#changed black to grey rgb codes because otherwise the black pieces wouldnt be able to be seen on black tiles
BLACK = (128, 128, 128)
BLUE = (0, 0, 255)

#pieces png
#pygame.transform.scale(image.load, resolution tuple)
BLACK_ROOK = pygame.transform.scale(pygame.image.load('images/black_rook.png'), (64, 64))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('images/black_knight.png'), (64, 64))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('images/black_bishop.png'), (64, 64))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('images/black_queen.png'), (64, 64))
BLACK_KING = pygame.transform.scale(pygame.image.load('images/black_king.png'), (64, 64))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('images/black_pawn.png'), (64, 64))

WHITE_ROOK = pygame.transform.scale(pygame.image.load('images/white_rook.png'), (64, 64))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('images/white_knight.png'), (64, 64))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('images/white_bishop.png'), (64, 64))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('images/white_queen.png'), (64, 64))
WHITE_KING = pygame.transform.scale(pygame.image.load('images/white_king.png'), (64, 64))
WHITE_PAWN = pygame.transform.scale(pygame.image.load('images/white_pawn.png'), (64, 64))