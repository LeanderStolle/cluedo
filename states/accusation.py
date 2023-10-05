# für Anklage muss man nicht in Raum stehen
# nur während des eigenen Spielzuges
# asuwählen der Anklagekarten
# nur einmal anklage erheben pro Spiel und Spieler
# vergleich mit Fallakte --> richtig? dann gewonnen, falsch? dann Spielaustritt (turn skip) aber Karten müssen trotzdem bei suspicion gezeigt werden
# 
#
#
#

import pygame
from states.state import State
from states.game_world import Game_World
from button import Button


class Accusation(State):
    def __init__(self, game):
        State.__init__(self, game)

        #Definiere Actions
        self.actions = {"pause": False, "note":False}