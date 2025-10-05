#This class would handle moving specific pieces, deleting specific pieces and drawing into the screen
import pygame
from checkersProject.constant import BLACK, WHITE, RED, ROWS, COLS, SQUARESIZE
from checkersProject.piece import Piece


class Board:
    def __init__(self):
        #A two dimesnional list for the board
        self.board = []
        #pieces the board starts with and keeping track
        self.redLeft = self.whiteLeft = 12
        #red kings and white kings equal to 0
        self.redKings =self.whiteKings = 0
        self.createBoard()

    def drawCheckerboard(self,win):
        #fill the enitre window with black
        win.fill(BLACK)
        #creating the checkboard pattern with red first then black
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQUARESIZE, col * SQUARESIZE, SQUARESIZE, SQUARESIZE))

    #evalutes and tries to prioritise pieces becoming kings quicker.
    def evaluate(self):
        return self.whiteLeft - self.redLeft + (self.whiteKings * 0.5 - self.redKings * 0.5)

    # gets all the pieces on the board according to a color.
    def getallPieces (self,color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
    # move a piece to a certain row and column
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.makeKing()
            if piece.color == WHITE:
                self.whiteKings += 1
            else:
                self.redKings += 1

    # returns a piece on the board
    def getPieces(self, row, col):
        return self.board[row][col]

    #Creating the pieces for the board, white up top black down below
    def createBoard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
            #basically on column 1 white is drawn first but on column 0 it is this this satisfy the condtion and thereafter
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.drawCheckerboard(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    #Removes pieces from the board
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.redLeft -= 1
                else:
                    self.whiteLeft -= 1

    def winner(self):
        if self.redLeft <= 0:
            return WHITE
        elif self.whiteLeft <= 0:
            return RED
        
        return None
    #gets the moves a piece can perform succesfully and correctly
    def getcorrectMoves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.kingpiece:
            moves.update(self._moveLeft(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._moveRight(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.kingpiece:
            moves.update(self._moveLeft(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._moveRight(row +1, min(row+3, ROWS), 1, piece.color, right))

        return moves
        
    # This determines how a piece can be moved either left or right
    def _moveLeft(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._moveLeft(r+step, row, step, color, left-1, skipped = last))
                    moves.update(self._moveRight(r+step, row, step, color, left+1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _moveRight(self, start, stop, step, color, right, skipped= []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._moveLeft(r+step, row, step, color, right-1, skipped = last))
                    moves.update(self._moveRight(r+step, row, step, color, right+1, skipped= last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        return moves
                



