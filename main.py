import pygame
from checkersProject.constant import WIDTH, HEIGHT, SQUARESIZE, RED, WHITE, BLACK
from checkersProject.board import Board
from checkersProject.gamestate import Gamestate
from abminimax.algorithm import minimaxAB, minimax

#SET UP PYGAME DISPLAY
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#SET CAPTION
pygame.display.set_caption('CHECKERS')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARESIZE
    col = x //SQUARESIZE
    return row, col

#DEFINE A MAIN FUNCTION(an event loop)
#Makes sure the program runs the same on all devices
def mainFunction():
    running = True
    
    clock = pygame.time.Clock()
    gamestate = Gamestate(WINDOW)


    while running:
        clock.tick(60)
        if gamestate.turn == WHITE:
            difficulty = 3
            value, newBoard = minimax(gamestate.getBoard(), difficulty, WHITE, gamestate)
            ## value, newBoard = minimaxAB(gamestate.getBoard(), difficulty, float('-inf'), float(+inf'), gamestate)
            gamestate.aiMove(newBoard)
        if gamestate.winner() != None:
            print(gamestate.winner())
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #if someone wins 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                gamestate.select(row, col)

        gamestate.update()
    pygame.quit()
     

mainFunction()
