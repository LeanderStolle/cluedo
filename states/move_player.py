# bewege Spielfigur für gewürfelte Augenzahl auf dem Spielbrett
# ODER Geheimgang benutzen
# ODER in Raum stehen bleiben
#
# --> suspicion state 



import pygame
from states.state import State
from states.game_world import Game_World
from button import Button


class MovePlayer(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        #Definiere Actions
        self.actions = {"pause": False, "note":False}


