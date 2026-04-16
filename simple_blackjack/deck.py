import random
from card import *


class Deck(): 
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')

    STANDARD_DICT = {'A':11, '2':2, '3':3, '4':4, '5':5,
    '6':6, '7':7, '8': 8, '9':9, '10':10,
    'J':10, 'Q':10, 'K':10}

    def __init__(self, window):
        self.startingDeckList = []
        self.playingDeckList = []
        self.build(window)
        self.shuffle()
        
    def build(self, window, rankValueDict=STANDARD_DICT):
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                oCard = Card(window, rank, suit, value)
                self.startingDeckList.append(oCard)

    def shuffle(self):
        self.playingDeckList = self.startingDeckList.copy()
        random.shuffle(self.playingDeckList)

    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise IndexError('No more cards')
        return self.playingDeckList.pop()