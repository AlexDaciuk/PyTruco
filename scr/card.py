#Class that defines an individual card, with it's number, figure and value

class Card:
    # Post: Creates the card with the especified number, figure and value 
    def __init__(self, number, figure, value):
        if (number > 0 and number < 13):
            self.number = number
    
        if figure in ["ORO", "BASTO", "ESPADA", "COPA"]: 
             self.figure = figure
             
        self.value = value


    def getNumber(self):
        return self.number

    def getFigure(self):
        return self.figure

    def getValue(self):
        return self.value
    
    
