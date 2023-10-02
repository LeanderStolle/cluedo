import pygame, os

from states.state import State


class Options(State):
    def __init__(self, game):
        State.__init__(self, game)
    
        

    def update(self, delta_time, actions):
        self.game.reset_keys()

    def render(self, screen):
        pass

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["pause"] = True  
                if event.key == pygame.K_SPACE:
                    self.actions["note"] = True   