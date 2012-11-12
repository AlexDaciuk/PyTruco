#we import random from choice
from random import choice
players = []

class deck:
    def __init__(self):
        global modifiable_deck
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
    
    def croupier(self, players = [], *args):
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
        self.card_quantity = card_quantity
        card_list = []
        self.card_list = card_list
        players.append(self)
        
    def show_cards(self):
        print(self.card_list)
        
deck1 = deck()

player_1 = player()

player_2 = player()

deck1.croupier(players)

player_1.show_cards()
player_2.show_cards()
