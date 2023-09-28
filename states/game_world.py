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
        

    def handle_click(self, x, y, board):
            for tile in board:
                if tile.contains_point(x, y):
                    print("Dieses Tile habe ich geklicked", tile.name)
                    return tile
                if tile.contains_point(x, y) & tile.type == "wall":
                    print("Hier kann man nicht hinlaufen", tile.name)
                    return tile
            return None

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  # Get the x, y position of the click
            clicked_tile = handle_click(x, y, board.board)





 
