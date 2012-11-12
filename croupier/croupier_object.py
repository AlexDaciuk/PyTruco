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
        modifiable_deck = deck
                

    def croupier(players = [], *args):
        for player in players:
            random_card = choice(modifiable_deck)
            player.card_list.append(random_card)
            modifiable_deck.remove(random_card)
            player.card_quantity += 1

    
    def print_deck(self):
        print(self.deck)


class player:
    def __init__(self):
        card_quantity = 0
        card_list = []
        
    

deck1 = deck()

deck1.print_deck()
