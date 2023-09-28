import pygame, os

from states.state import State
from states.pause_menu import PauseMenu
from states.note import Note
from Tile import Tile


class Game_World(State):
    def __init__(self, game):
        State.__init__(self, game)
        #TO-DO: Implentieren der Tiles
        #self.map_img_unscaled = pygame.image.load(os.path.join(self.game.assets_dir, "map", "clue_board1.jpg"))
        #self.map_img = pygame.transform.scale(self.map_img_unscaled, (960, 960))
        self.board = [Tile("Kitchen", "Room", 0, 0, 150, 150, (255,248,220)),Tile('Wall', 'wall', 150, 0, 50, 150, (0,0,0))]


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
        self.draw_board(screen)
        

    def handle_click(self, x, y, board):
            for tile in board:
                if tile.contains_point(x, y):
                    print("Dieses Tile habe ich geklicked", tile.name)
                    return tile
                if tile.contains_point(x, y) and tile.type == "wall":
                    print("Hier kann man nicht hinlaufen", tile.name)
                    return tile
            return None
    
    def draw_board(self, screen):
        for row in range(len(self.board)):
            tile = self.board[row]
            pygame.draw.rect(screen,tile.color, (tile.x, tile.y, tile.width, tile.height))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["pause"] = True  
                if event.key == pygame.K_SPACE:
                    self.actions["note"] = True    
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x, self.y = event.pos  # Get the x, y position of the click
                clicked_tile = self.handle_click(self.x, self.y, self.board)
                print(clicked_tile)

    
   




 
