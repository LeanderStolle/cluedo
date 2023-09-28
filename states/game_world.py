import pygame, os

from states.state import State
from states.pause_menu import PauseMenu
from states.note import Note

class Game_World(State):
    def __init__(self, game):
        State.__init__(self, game)
        #TO-DO: Implentieren der Tiles
        self.map_img_unscaled = pygame.image.load(os.path.join(self.game.assets_dir, "map", "clue_board1.jpg"))
        self.map_img = pygame.transform.scale(self.map_img_unscaled, (960, 960))


    def update(self, delta_time, actions):
        if actions["pause"]:
            new_state = PauseMenu(self.game)
            new_state.is_open = True
            new_state.enter_state()
        elif actions["note"]:
            new_state = Note(self.game)
            new_state.is_open = True
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, screen):
        screen.blit(self.map_img, (0,0))