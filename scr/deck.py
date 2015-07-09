# Class that defines a deck of cards, basically is a list with all the cards
import Card

class Deck():

    def __init__():
    # Iterate throught all twelve numbers                                                                                                                 
        for number in range(1,12,1):

            # Iterate all four figures                                                                                                                        
            for figure in ("ORO", "BASTO", "ESPADA", "COPA"):

                # Its horrible, but I cant think of a better way to assign                                                                                    
                # values to all the cards                                                                                                                     
        	if (number == 1):
                    if ( figure == "ESPADA" ):
		        value = 1
                    else if (figure == "BASTO"):
                        value = 2
                    else:
                        value = 7

                else if (number == 2):
                    value = 6

		else if (number == 3):
                    value = 5

		else if (number == 4):
                    value = 14

                else if (number == 5):
                    value = 13

		else if (number == 6):
                    value = 12

		else if (number == 7):
                    if ( figure == "ESPADA"):
		        value = 3
                    else if (figure == "ORO"):
		        value = 4
                    else:
                        value = 11

		else if ( number == 8 or number == 9):
                    pass

		else if ( number == 10 ):
                    value = 10

        	else if ( number == 11):
                    value = 9

        	else if ( number == 12):
                    value = 8

		# We dont use 8s and 9s for this particular card game                                                                                         
                if ( number != 8 or number != 9):
                    cardList.append( card(number, figure, value) )
                    
   def getCompleteDeck():
   	return self.cardList
