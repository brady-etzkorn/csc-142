# pygame demo 6(b) - using the Ball class, bounce many balls

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  
game_over = False
click_processed = False
player_score = 0
start_time = pygame.time.get_ticks()
last_seconds = 0
new_ball = -1


# 4 - Load assets: image(s), sounds, etc.

score_board = pygame.Rect(0, 0, 160, 60)
font = pygame.font.Font(None, 36)
time_box = pygame.Rect(200, 70, 200, 50)


# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # append the new Ball to the list of Balls   

def draw_score(screen, player_score):
    # Creating the score board
        pygame.draw.rect(screen, (50, 50, 50), score_board)
        pygame.draw.rect(screen, (255, 255, 255), score_board, 3)

    # Creating the score text
        text = font.render(f"Score:{player_score}", True, (255, 255, 255))
        screen.blit(text, (score_board.x + 10, score_board.y + 10))

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

        if event.type == pygame.MOUSEBUTTONDOWN and not click_processed:
            for Oball in ballList:
                if Oball.ballRect.collidepoint(event.pos):
                    player_score += 1
                print("Score:",player_score)
            click_processed = True      
        
        if event.type == pygame.MOUSEBUTTONUP:
            click_processed = False
    
    
    # Ending the game at 15 seconds
    current_time = pygame.time.get_ticks()

    if not game_over:
        last_seconds = int((current_time - start_time) / 1000)

    if last_seconds >= 15 and not game_over:
        game_over = True
        elapsed_seconds = last_seconds
        ballList = []

 # 8 - Do any "per frame" actions
    if not game_over and last_seconds > new_ball:
            new_ball = last_seconds
            ballList.append(Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT))

    if not game_over :
        for oBall in ballList:
            oBall.update()  # tell each Ball to update itself
            
# 9 - Clear the window before drawing it again
    window.fill(BLACK)
    draw_score(window,player_score)

    pygame.draw.rect(window, (50, 50, 50), (1, 70, 200, 50))
    pygame.draw.rect(window, (255, 255, 255), (1, 70, 200, 50), 3)

    live_time_text = font.render(f"Time: {last_seconds}s", True, (255, 255, 255))
    window.blit(live_time_text, (10, 80))
    
    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()   # tell each Ball to draw itself

    if game_over:
        over_text = font.render(f"Final Score: {player_score}", True, (255, 255, 255))
        window.blit(over_text, (200, 200))

 # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait