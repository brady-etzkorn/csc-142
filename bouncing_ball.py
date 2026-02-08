
# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
click_processed = False
game_over = False
 
# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('images/ball.png')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)

score_board = pygame.Rect(0, 0, 160, 60)
font = pygame.font.Font(None, 36)

# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# Making the players score
player_score = 0

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
        # Clicked the close button? Quit pygame and end the program  
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN and not click_processed:
            if ballRect.collidepoint(event.pos):
                player_score += 1
                print("Score:",player_score)
                ySpeed = random.randint(1,5)
                xSpeed = random.randint(1,5)
            click_processed = True
    
        if event.type == pygame.MOUSEBUTTONUP:
            click_processed = False
    
    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction
        bounceSound.play()

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction
        bounceSound.play()
    
    # Ending the game after player clicks 5 times
    if player_score == 5 and not game_over:
        game_over = True
        end_time = pygame.time.get_ticks()
        elapsed_seconds = (end_time - start_time) / 1000

    # Freeze the ball immediately
        xSpeed = 0
        ySpeed = 0
    
    if not game_over:
        ballRect.left += xSpeed
        ballRect.top += ySpeed
    else:
        ballRect.left = -1000
        ballRect.top = -1000
        
    # Update the rectangle of the ball, based on the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

     # 10 - Draw the window elements
    window.fill(BLACK)
    window.blit(ballImage, ballRect)
    draw_score(window,player_score)
    pygame.display.update()

    if game_over:
        time_text = font.render(f"Time: {elapsed_seconds:.2f}s", True, (255, 255, 255))
        window.blit(time_text, (200, 200))


    # 12 - Slow things down a bit
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)  

