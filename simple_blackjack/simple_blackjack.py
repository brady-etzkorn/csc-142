import pygame
import sys
import pygwidgets
from deck import *
from card import *
from pygame.locals import *



pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Simple Blackjack')

background = pygwidgets.Image(window, (0, 0),
                              'blackjack_images/background.png')
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
        self.gameOver = False
        self.deck = Deck(window)

        
        self.messageText = pygwidgets.DisplayText(window, (50, 460),
                                                    '', width=900, justified='center',
                                                    fontSize=36, textColor=BLACK)
        
        self.cardXPositionsList = []
        thisLeft = Game.CARDS_LEFT
# Calculate the x positions of all cards, once
        for cardNum in range(Game.NCARDS):
            self.cardXPositionsList.append(thisLeft)
            thisLeft = thisLeft + Game.CARD_OFFSET

        self.reset() # start a round of the game
        self.result = ''
    
    def start_round(self):

        self.playerHand = []
        self.dealerHand = []

        self.playerHand.append(self.deck.getCard())
        self.playerHand.append(self.deck.getCard())
    
        self.dealerHand.append(self.deck.getCard())
        self.dealerHand.append(self.deck.getCard())

        

    def reset(self): # this method is called when a new round starts
        self.result = ""
        self.gameOver = False
        self.playerTurn = True
        
        self.playerHand = []
        self.dealerHand = []
        self.cardList = []
        self.deck.shuffle()

        self.playerHand.append(self.deck.getCard())
        self.playerHand.append(self.deck.getCard())
    
        self.dealerHand.append(self.deck.getCard())
        self.dealerHand.append(self.deck.getCard())


        for cardIndex in range(0, Game.NCARDS): # deal out cards
            oCard = self.deck.getCard()
            self.cardList.append(oCard)
            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))

        self.showCard(0)
        self.cardNumber = 0
        self.currentCardName, self.currentCardValue = \
                                self.getCardNameAndValue(self.cardNumber)

        self.messageText.setValue('Do you want to hit or stand?')

        if self.handValue(self.playerHand) == 21:
            self.result = "Blackjack! Player Wins!"
            self.gameOver = True
        
        playerHand = self.handValue(self.playerHand)
        dealerHand = self.handValue(self.dealerHand)


    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()
    
    def PlayerHit(self):
        card = self.deck.getCard()
        self.playerHand.append(card)

        x = 100 + (len(self.playerHand) - 1) * 120
        y = 500
        card.setLoc((x, y))

        card.reveal()

        if self.handValue(self.playerHand) > 21:
            self.gameOver = True
            self.messageText.setValue("Bust! You lose.")

    def PlayerStand(self):
        self.playerTurn = False

    # Reveal dealer card (if hidden)
        self.dealerHand[0].reveal()

    # Dealer draws
        while self.handValue(self.dealerHand) < 17:
            self.dealerHand.append(self.deck.getCard())

    # Determine winner
        playerTotal = self.handValue(self.playerHand)
        dealerTotal = self.handValue(self.dealerHand)

        if dealerTotal > 21:
            self.result = "Player Wins! Dealer Busts"
        elif dealerTotal > playerTotal:
            self.result = "Dealer Wins"
        elif dealerTotal < playerTotal:
            self.result = "Player Wins"
        elif playerTotal == 21:
            self.result = "Player Wins"
        else:
            self.result = "Push (Tie)"

        self.gameOver = True
    
    def handValue(self, hand):
        total = 0
        aces = 0

        for card in hand:
            value = card.getValue()
            total += value

        if card.getRank() == 'A':
            aces += 1

    # Adjust for aces
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    def NewGame(self):
        self.playerHand = []
        self.dealerHand = []

        oGame.start_round()

    
    
# Tell each card to draw itself
    def draw(self, screen):

        x = 100
        for card in self.playerHand:
            screen.blit(card.image, (x, 400))

            x += 80

        x = 100
        y = 100

        for card in self.dealerHand:
            screen.blit(card.image,(x,y))
            x += 80

        self.messageText.draw()

        print(type(screen))

        font = pygame.font.SysFont(None, 40)
        textSurface = font.render(self.result, True, (0, 0, 0))
        screen.blit(textSurface, (400, 300))
        

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
    oGame.draw(screen)

# Draw remaining user interface components
    newGameButton.draw()
    hitButton.draw()
    standButton.draw()
    quitButton.draw()

# 11 - Update the window
    pygame.display.update()
# 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)

