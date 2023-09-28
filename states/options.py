import pygame, os

from states.state import State


class Options(State):
    def __init__(self, game):
        State.__init__(self, game)
    
        

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, screen):
        pass