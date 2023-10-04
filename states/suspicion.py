# checken ob ein Spieler einen Raum betreten hat oder in einem Raum steht
# man verdächtigt immer den Raum in dem man steht, eine Waffe und eine Person
# bewege den verdächtigten Spieler + Tatwaffe in den Raum
# der Spieler Links neben dir zeigt dir nun EINE verdächtigte Karte solange er sie besitzt, bei mehreren nur eine zeigen
# wenn der Spieler links von dir keine dieser Karten hat geht es im Uhrzeigersinn weiter, sobald eine Karte gezeigt wurde endet die Befragung
#
# --> accusation state
# --> note state





import pygame
from states.state import State
from states.game_world import Game_World
from button import Button


class Suspicion(State):
    def __init__(self, game):
        State.__init__(self, game)

        #Definiere Actions
        self.actions = {"pause": False, "note":False}