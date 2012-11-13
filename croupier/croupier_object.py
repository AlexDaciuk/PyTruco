#we import random from choice
from random import choice
import sys
players = []

class deck:
    def __init__(self):

        deck = []
        self.deck = deck
        types = ["oro","basto","espada","copas"]

        for card_type in types:
            for i in list(range(1,13,1)):
                if i == 8 or i == 9:
                    pass
                else:
                    deck.append(str(i)+"_de_"+card_type)

        modifiable_deck = deck
        self.modifiable_deck = modifiable_deck
        
    def croupier(self, players = [], *args):
        for player in players:
            for i in range(3):
                random_card = choice(self.modifiable_deck)
                player.card_list.append(random_card)
                self.modifiable_deck.remove(random_card)
                player.card_quantity += 1
            
    def print_deck(self):
            print(self.deck)
                    
                    
class player:
    def __init__(self):
        card_quantity = 0
        self.card_quantity = card_quantity

        card_list = []
        self.card_list = card_list

        players.append(self)
        
    def show_cards(self):
        print(self.card_list)

try:
    sys.argv[1] == 4
    deck1 = deck()
    quantity = list(range(1,(int(sys.argv[1]))+1))
    for i in quantity:
        player_i = player() 
    deck1.croupier(players)
    
                    
except(IndexError):
    deck1 = deck()
    quantity = list(range(1,3))
    for i in quantity:
        player_i = player()
    deck1.croupier(players)
    

