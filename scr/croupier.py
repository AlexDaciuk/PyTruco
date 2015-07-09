#Class that handles the cards to the server

import deck
import random


class Croupier():

    # Class constructor, it creates a full deck
    def __init__(self):
        self.deck = deck.Deck()

    # We duplicate the original deck to work with the duplicate one
    def startGiving(self):
        self.workDeck = self.deck

    # Method that returns a list of 3 cards 'randomly' picked 
    def givePlayer(self):

        self.playerCardSet = []
        
        # First we reverse the deck, just to get a little more random
        #self.workDeck.reverse()

        # We pick 3 cards and put them on a list
        for i in range(1,3,1):
            self.playerCardSet.append( self.workDeck.getRandomCard() ) )

        return self.playerCardSet
        
        
