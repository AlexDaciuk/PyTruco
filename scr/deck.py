# Class that defines a deck of cards, basically is a list with all the cards
import card

class Deck():

    def __init__(self):
    # Iterate throught all twelve numbers                                                                                                                 
        self.cardList = []
        
        for number in range(1,12,1):

            # Iterate all four figures                                                                                                                        
            for figure in ["ORO", "BASTO", "ESPADA", "COPA"]:

                # Its horrible, but I cant think of a better way to assign                                                                                    
                # values to all the cards                                                                                                                     
        	if (number == 1):
                    if [ figure == "ESPADA" ]:
		        value = 1
                    elif [figure == "BASTO"]:
                        value = 2
                    else:
                        value = 7

                elif (number == 2):
                    value = 6

		elif (number == 3):
                    value = 5

		elif (number == 4):
                    value = 14

                elif (number == 5):
                    value = 13

		elif (number == 6):
                    value = 12

		elif (number == 7):
                    if (figure == "ESPADA"):
		        value = 3
                    elif (figure == "ORO"):
		        value = 4
                    else:
                        value = 11

		elif ( number == 8 or number == 9):
                    pass

		elif ( number == 10 ):
                    value = 10

        	elif ( number == 11):
                    value = 9

        	elif ( number == 12):
                    value = 8

		# We dont use 8s and 9s for this particular card game                                                                                         
                if ( number != 8 or number != 9):
                    self.cardList.append( card.Card(number, figure, value) )
                    

    def getCompleteDeck():
   	return self.cardList


    def getRandomCard():
        
