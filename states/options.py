import pygame, os

from states.state import State


class Options(State):
    def __init__(self, game):
        State.__init__(self, game)
        

    def update(self, delta_time, actions):
        self.game.res

    def render(self, screen):
        screen.blit(self.map_img, (0,0))