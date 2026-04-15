import pygame
import sys
import pygwidgets
from deck import *
from card import *
from pygame.locals import *



pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Simple Blackjack')

background = pygwidgets.Image(window, (0, 0),
                              'background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
                                    'New Game', width=100, height=45)
hitButton = pygwidgets.TextButton(window, (540, 520),
                                    'Hit', width=120, height=55)
standButton = pygwidgets.TextButton(window, (340, 520),
                                    'Stand', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                                    'Quit', width=100, height=45)

class Game():
    CARDS_LEFT = 75
    NCARDS = 8
    CARD_OFFSET = 110
    CARDS_TOP = 300
    def __init__(self, window):

        self.window = window
        self.playerHand = []
        self.dealerHand = []
        self.gameOver = False

    
    
        self.oDeck = Deck(self.window)
        
        self.messageText = pygwidgets.DisplayText(window, (50, 460),
                                                    '', width=900, justified='center',
                                                    fontSize=36, textColor=WHITE)
        
        self.cardXPositionsList = []
        thisLeft = Game.CARDS_LEFT
# Calculate the x positions of all cards, once
        for cardNum in range(Game.NCARDS):
            self.cardXPositionsList.append(thisLeft)
            thisLeft = thisLeft + Game.CARD_OFFSET

        self.reset() # start a round of the game

    def reset(self): # this method is called when a new round starts
        self.playerHand = []
        self.dealerHand = []
        self.cardList = []
        self.oDeck.shuffle()
        for cardIndex in range(0, Game.NCARDS): # deal out cards
            oCard = self.oDeck.getCard()
            self.cardList.append(oCard)
            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))

        self.showCard(0)
        self.cardNumber = 0
        self.currentCardName, self.currentCardValue = \
                                self.getCardNameAndValue(self.cardNumber)

        self.messageText.setValue('Starting card is ' + self.currentCardName +
                                    '. Will the next card be higher or lower?')

    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()
    
    def PlayerHit(self):
        card = self.oDeck.getCard()
        self.playerHand.append(card)

        x = 100 + (len(self.playerHand) - 1) * 120
        y = 500
        card.setLoc((x, y))

        card.reveal()

        if self.handValue(self.playerHand) > 21:
            self.gameOver = True
            self.messageText.setValue("Bust! You lose.")

    def PlayerStand(self):
    # Dealer hits until 17
        while self.handValue(self.dealerHand) < 17:
            card = self.oDeck.getCard()
            self.dealerHand.append(card)
            card.reveal()

            x = 100 + (len(self.dealerHand) - 1) * 120
            y = 150
            card.setLoc((x, y))

            self.gameOver = True
            self.checkWinner()

    def checkWinner(self):
        player = self.handValue(self.playerHand)
        dealer = self.handValue(self.dealerHand)

        if dealer > 21:
            self.messageText.setValue("Dealer busts! You win!")
        elif player > dealer:
            self.messageText.setValue("You win!")
        elif player < dealer:
            self.messageText.setValue("You lose!")
        else:
            self.messageText.setValue("Push!")
    
    def handValue(self, hand):
        total = 0
        for card in hand:
            total += card.getValue()
        return total
    
    def draw(self): 
# Tell each card to draw itself
        def draw(self):
            for card in self.playerHand:
                card.draw()

            for card in self.dealerHand:
                card.draw()

        self.messageText.draw()
        
        def draw(self):
            if self.revealed:
                self.window.blit(self.image, self.loc)
            else:
                self.window.blit(self.backImage, self.loc)

oGame = Game(window)

# 6 - Loop forever
while True:
# 7 - Check for and handle events
    for event in pygame.event.get():
        if ((event.type == QUIT) or
        ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
        (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()
        
        if newGameButton.handleEvent(event):
            oGame.reset()
            standButton.enable()
            hitButton.enable()

        if hitButton.handleEvent(event):
            oGame.PlayerHit()
        
        if standButton.handleEvent(event):
            oGame.PlayerStand()
# 8 - Do any "per frame" actions
# 9 - Clear the window before drawing it again
    background.draw()



   

# 10 - Draw the window elements
# Tell the game to draw itself
    oGame.draw()

# Draw remaining user interface components
    newGameButton.draw()
    hitButton.draw()
    standButton.draw()
    quitButton.draw()

# 11 - Update the window
    pygame.display.update()
# 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)

