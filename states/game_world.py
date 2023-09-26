import pygame, os

from states.state import State

class Game_World(State):
    def __init__(self, game):
        State.__init__(self, game)
        #TO-DO: Implentieren der Tiles
        self.map_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "clue_board1.jpg"))

    def update(self, delta_time, actions):
        pass

    def render(self, screen):
        screen.blit(self.map_img, (0,0))