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
    pygame.font.init() # Initialize fonts
    # Use a system font that looks blocky, or a path to a .ttf file
    font = pygame.font.SysFont("Courier", 50, bold=True) 
    text_surface = font.render("CHOOSE YOUR PIECE", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    running = True
    clock = pygame.time.Clock()
    gamestate = Gamestate(WINDOW)
    
    # NEW: Selection state variables
    menu_active = True
    end_active = False
    user_color = None
    winner_text = ""


    while running:
        clock.tick(60)

        if menu_active:
            WINDOW.fill(BLACK) 
            
            # Draw the 8-bit Text
            WINDOW.blit(text_surface, text_rect)
            
            # Draw two "buttons" (The pieces)
            red_piece = pygame.draw.circle(WINDOW, RED, (WIDTH//4, HEIGHT//2), 50)
            white_piece = pygame.draw.circle(WINDOW, WHITE, (3*WIDTH//4, HEIGHT//2), 50)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    menu_active = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    
                    # Using the circle rects for cleaner collision
                    if red_piece.collidepoint(pos):
                        user_color = RED
                        gamestate.turn = RED
                        menu_active = False
                        gamestate.update() # Draw the starting board
                        pygame.display.update()
                        pygame.time.delay(500)
                        pygame.event.clear()
                    elif white_piece.collidepoint(pos):
                        user_color = WHITE
                        gamestate.turn = RED
                        menu_active = False
                        gamestate.update() # Draw the starting board
                        pygame.display.update()
                        pygame.time.delay(500)
                        pygame.event.clear()
        elif end_active:
            WINDOW.fill(BLACK)
            
            # 1. Display Result Text
            result_surf = font.render(winner_text, True, WHITE)
            result_rect = result_surf.get_rect(center=(WIDTH // 2, HEIGHT // 3))
            WINDOW.blit(result_surf, result_rect)
            
            # 2. Draw "START AGAIN" Button
            button_font = pygame.font.SysFont("Courier", 30, bold=True)
            btn_surf = button_font.render("START AGAIN", True, BLACK)
            # Create a background rectangle for the button
            btn_rect = pygame.Rect(0, 0, 250, 60)
            btn_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            
            pygame.draw.rect(WINDOW, WHITE, btn_rect) # Button background
            WINDOW.blit(btn_surf, btn_surf.get_rect(center=btn_rect.center))
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_rect.collidepoint(event.pos):
                        # RESET EVERYTHING to go back to color selection
                        gamestate = Gamestate(WINDOW) # Fresh board
                        menu_active = True
                        end_active = False
                        user_color = None
        
        else:
            if gamestate.turn != user_color: 
                difficulty = 3
                # 1. Figure out what color the AI is
                ai_color = WHITE if user_color == RED else RED
                
                # 2. Pass True for the 'maxplayer' argument
                # 3. Ensure your minimax function in algorithm.py is updated to accept ai_color
                value, newBoard = minimax(gamestate.getBoard(), difficulty, True, gamestate, ai_color)
                gamestate.aiMove(newBoard)

            winner = gamestate.winner()
            if winner != None:
                winner_text = "RED WINS!" if winner == RED else "WHITE WINS!"
                if winner == "DRAW": # If you have draw logic
                    winner_text = "IT'S A DRAW!"
                end_active = True # This will trigger the end screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Only allow clicking if it IS the user's turn
                if event.type == pygame.MOUSEBUTTONDOWN and gamestate.turn == user_color:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    gamestate.select(row, col)

            gamestate.update()

    pygame.quit()
     

mainFunction()
