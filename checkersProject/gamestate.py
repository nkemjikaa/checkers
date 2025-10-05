import pygame
from checkersProject.constant import RED, WHITE, GREEN, SQUARESIZE
from checkersProject.board import Board

class Gamestate:
    def __init__(self,win):
        self._init()
        self.win = win
    
    #This function updates the display and draws it
    def update(self):
        self.board.draw(self.win)
        self.drawvalidMoves(self.validMoves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.validMoves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()
    #This function allows us to successfully move a piece around according to constraints
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.getPieces(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.validMoves = self.board.getcorrectMoves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.getPieces(row, col)
        if self.selected and piece == 0 and (row, col) in self.validMoves:
            self.board.move(self.selected, row, col)
            skipped = self.validMoves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.changeTurn()
        else:
            return False

        return True
    #This shows the moves a player can perform in green
    def drawvalidMoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARESIZE + SQUARESIZE//2, row * SQUARESIZE + SQUARESIZE//2),15)

    # Changes turn when a player has moved
    def changeTurn(self):
        self.validMoves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def getBoard(self):
        return self.board

    def aiMove(self, board):
        self.board = board
        self.changeTurn()  
    