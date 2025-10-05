import pygame
from copy import deepcopy
from checkersProject.board import Board
from checkersProject.gamestate import Gamestate
from checkersProject.constant import RED, WHITE

#position is the current postion of the player playing
#depth how far is the tree. this would be decremented
#maxplayer is true the value is max if maxplayer is false then the value is min
#minimax algorithm
def minimax(position, depth, maxplayer, gamestate):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if maxplayer:
        maxEvaluation = float('-inf')
        bestMove = None
        for move in getallMoves(position, WHITE, gamestate):
            evaluation = minimax(move, depth-1, False, gamestate)[0]
            maxEvaluation = max(maxEvaluation, evaluation)
            if maxEvaluation == evaluation:
                bestMove = move
        return maxEvaluation, bestMove

    else:
        minEvaluation = float('+inf')
        bestMove = None
        for move in getallMoves(position, RED, gamestate):
            evaluation = minimax(move, depth-1, True, gamestate)[0]
            minEvaluation = min(minEvaluation, evaluation)
            if minEvaluation == evaluation:
                bestMove = move
        return minEvaluation, bestMove
        
#minimax algorithm with alpha beta pruning
def minimaxAB(position, depth, alpha, beta, maxplayer, gamestate):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if maxplayer:
        maxEvaluation = float('-inf')
        bestMove = None
        for move in getallMoves(position, WHITE, gamestate):
            evaluation = minimaxAB(move, depth-1, alpha, beta, False, gamestate)[0]
            maxEvaluation = max(maxEvaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                bestMove = move
                break
        return maxEvaluation, bestMove

    else:
        minEvaluation = float('+inf')
        bestMove = None
        for move in getallMoves(position, RED, gamestate):
            evaluation = minimaxAB(move, depth-1,alpha, beta, True, gamestate)[0]
            minEvaluation = min(minEvaluation, evaluation)
            if beta <= alpha:
                bestMove = move
                break
        return minEvaluation, bestMove

def simulateMoves(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def drawMoves(gamestate, board, piece):
    correctMoves = board.getcorrectMoves(piece)
    board.draw(gamestate.win)
    pygame.draw.circle(gamestate.win, (0,255, 0), (piece.x, piece.y), 50, 5) 

# get all the moves that can be done on the board
def getallMoves(board, color, gamestate):
    moves = []

    for piece in board.getallPieces(color):
        correctMoves = board.getcorrectMoves(piece)
        for move, skip in  correctMoves.items():
            drawMoves(gamestate, board, piece)
            temporaryBoard = deepcopy(board)
            temporaryPiece = temporaryBoard.getPieces(piece.row, piece.col)
            newBoard = simulateMoves(temporaryPiece, move, temporaryBoard, gamestate, skip)
            moves.append(newBoard)

    return moves



