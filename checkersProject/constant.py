#A constant file to keep all our constants variables so changing varaibles is more conveient and less tedious
import pygame

#1000 PIXELS HIGH 1000 PIXELS WIDE
WIDTH = 700
HEIGHT = 700

#AMOUNT OF ROWS AND COLUMNS ON THE BOARD. A typical checkers board is 8 by 8
ROWS = 8
COLS = 8

#SIZE OF A SQUARE ON THE BOARD
SQUARESIZE = WIDTH// COLS

#COLOURS FOR THE BOARD. RED SQUARES, BLACK SQUARES, BLACK PIECES, WHITE PIECES, GREEN NAVIGATION FOR CORRECT MOVES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 255)
SILVER = (192,192,192)

CROWN = pygame.transform.scale(pygame.image.load('assets/kingcrown.png'), (45, 30))
