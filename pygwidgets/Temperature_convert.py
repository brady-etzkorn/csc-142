# This program converts temperatures between fahrenheit and celsius.
# David Kopec
# 1 - Import libraries
import os
import sys
# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
from pygame.locals import *
import pygwidgets
# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock() # create a clock object
# 4 - Load assets: image(s), sounds, etc.
convertedDisplay = pygwidgets.DisplayText(window, (0, 20), '32',
fontSize=36, width= 640, textColor=BLACK,
justified='center')
userInputText = pygwidgets.InputText(window, (20, 100), '0',
textColor=WHITE, backgroundColor=BLACK,
fontSize=24, width=250)
celsiusRadio = pygwidgets.TextRadioButton(window, (500, 320), 'Default Group',
'Celsius',
value=True)
fahrenheitRadio = pygwidgets.TextRadioButton(window, (500, 360), 'Default Group',
'Fahrenheit',
value=False)
conversionButton = pygwidgets.TextButton(window, (500, 430), 'Convert')

# 5 - Initialize variables
def convert(original_degrees, celsius):
    print("I'm in convert")
    
    value = float(userInputText.getText())

    if celsius:  # Celsius → Fahrenheit
        result = (value - 32) * 5/9
        convertedDisplay.setText(f"{result:.2f}")
    else:                        
        result = value * 9/5 + 32
        convertedDisplay.setText(f"{result:.2f}")


# 6 - Loop forever
while True:
# 7 - Check for and handle events
    for event in pygame.event.get():
# check if the event is the close button
        if event.type == pygame.QUIT:
# if it is quit, the program
            pygame.quit()
            sys.exit()

        userInputText.handleEvent(event)
        celsiusRadio.handleEvent(event)
        fahrenheitRadio.handleEvent(event)

        if conversionButton.handleEvent(event): # clicked
            text = userInputText.getText()
    
            if celsiusRadio.getValue():
                convert(text, True)
            else:
                convert(text,False)
        
# 8 Do any "per frame" actions

# 9 - Clear the window
    pygame.draw.rect(window, GRAY, (0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
# 10 - Draw all window elements
    userInputText.draw()
    celsiusRadio.draw()
    fahrenheitRadio.draw()
    conversionButton.draw()
    convertedDisplay.draw()
# 11 - Update the window
    pygame.display.update()
# 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND) # make pygame wait

