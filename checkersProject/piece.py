#This class is for the pieces white and red checkers pieces.
import pygame
from checkersProject.constant import RED, WHITE, SILVER, SQUARESIZE, COLS, ROWS, CROWN

class Piece:
    PADDING = 18
    OUTLINE = 2

    def __init__(self,row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.kingpiece = False
        self.x = 0
        self.y = 0
        self.calculatePos()

    #calculating postion of pieces which should be in the middle of the square the piece is placed on
    def calculatePos(self):
        self.x = SQUARESIZE * self.col + SQUARESIZE // 2
        self.y = SQUARESIZE * self.row + SQUARESIZE // 2

    def makeKing(self):
        self.kingpiece = True
    

    #This would draw the pieces for the board since some pieces share the same colout as the board we would need a colour which outlines the piece so the piece can be seen properly
    def draw(self, win):
        radius = SQUARESIZE//2 - self.PADDING
        pygame.draw.circle(win, SILVER, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.kingpiece:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self,row, col):
        self.row = row
        self.col = col
        self.calculatePos()



    