import pygame


class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('blackjack_images/backofcard.jpg')
    BACK_OF_CARD_IMAGE = pygame.transform.scale(BACK_OF_CARD_IMAGE, (80, 120))

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value

        imagePath = f'blackjack_images/{suit.lower()}_{str(rank)}.png'

        # Face image
        self.faceImage = pygame.image.load(imagePath).convert_alpha()
        self.faceImage = pygame.transform.scale(self.faceImage, (80, 120))

        # Back image (shared)
        self.backImage = Card.BACK_OF_CARD_IMAGE

        # Position (IMPORTANT)
        self.x = 0
        self.y = 0

        # Start face up
        self.image = self.faceImage
        self.isFaceUp = True

    def setLoc(self, loc):
        self.x = loc[0]
        self.y = loc[1]

    def getLoc(self):
        return (self.x, self.y)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def conceal(self):
        self.image = self.backImage
        self.isFaceUp = False

    def reveal(self):
        self.image = self.faceImage
        self.isFaceUp = True

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank