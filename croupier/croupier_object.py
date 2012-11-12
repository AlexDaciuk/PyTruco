#we import random from choice
from random import choice

class deck:
    def __init__(self):
        deck = []
        self.deck = deck
        types = ["oro","basto","espada","copas"]
        for card_type in types:
            for i in list(range(1,13,1)):
                deck.append(str(i)+"_de_"+card_type)
        
                
    def print_deck(self):
        print(self.deck)




deck1 = deck()

deck1.print_deck()
