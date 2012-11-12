#we import random from choice
from random import choice

#we create a list with all the cards (spanish playing cards)
deck = ["uno_de_espadas","dos_de_espadas","tres_de_espadas","cuatro_de_espadas","cinco_de_espadas","seis_de_espadas","siete_de_espadas","diez_de_espadas","once_de_espadas","doce_de_espadas", "uno_de_oro","dos_de_oro","tres_de_oro","cuatro_de_oro","cinco_de_oro","seis_de_oro","siete_de_oro","diez_de_oro","once_de_oro","doce_de_oro","uno_de_basto","dos_de_basto","tres_de_basto","cuatro_de_basto","cinco_de_basto","seis_de_basto","siete_de_basto","diez_de_basto","once_de_basto","doce_de_basto","uno_de_copas","dos_de_copas","tres_de_copas","cuatro_de_copas","cinco_de_copas","seis_de_copas","siete_de_copas","diez_de_copas","once_de_copas","doce_de_copas"]

#we duplicate the deck to modify it 
modifiable_deck = list(deck)

#we set on 0 the quantity of both players cards
player_1_cards_quantity = 0
player_2_cards_quantity = 0

#we define 2 void lists for the actually cards of both players
player_1_cards = []
player_2_cards = []
distribute = 1

#this is the for that "distribute" the cards for player 1
#it just pick a card for the modifiable_deck and puts into the player 1 list and remove it from the deck until player 1 has 3 cards

if distribute == 1:
    while player_1_cards_quantity < 3:
        random_card = choice(modifiable_deck)
        player_1_cards.append(random_card)
        modifiable_deck.remove(random_card)
        player_1_cards_quantity += 1
        
# just the same thing for player 2

    while player_2_cards_quantity < 3:
        random_card = choice(modifiable_deck)
        player_2_cards.append(random_card)
        modifiable_deck.remove(random_card)
        player_2_cards_quantity += 1
        


print("\nPlayer 1 cards: ",player_1_cards)
print("\nPlayer 2 cards: ",player_2_cards)


