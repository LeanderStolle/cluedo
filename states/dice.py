# wirf 2 Würfel 
# FÜr jede gwürfelte Lupe wird eine Beweiskarte gezogen
# wenn cluedo Karte gezogen dann auf Notizzettel markieren
# gespielte Karten müssen zurück unter den Stapel
# --> movePlayer state

import pygame, random
from states.state import State


class Dice(State):
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0


        #Definiere Actions
        self.actions = {"pause": False, "note":False}

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)

    def get_sum(self):
        return self.dice1 + self.dice2

    def get_result(self):
        return self.dice1, self.dice2
    
    #def checkForOne(self):
    #    result = self.get_result()
    #    if 1 in result:
    #        if result == (1, 1):
    #            card1 = card_stack.draw_card()
    #            card2 = card_stack.draw_card()
    #            print(f"You rolled two 1s! You drew two cards: {card1} and {card2}")
    #        else:
    #            card = card_stack.draw_card()
    #            print(f"You rolled a 1! You drew a card: {card}")
    #    else:
    #        print(f"You rolled: {result[0]} and {result[1]}")
        
