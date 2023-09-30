import pygame, os

from states.state import State
from states.pause_menu import PauseMenu
from states.note import Note
from Tile import Tile
from Colors import *

class Game_World(State):
    def __init__(self, game):
        State.__init__(self, game)
        #TO-DO: Implentieren der Tiles
        #self.map_img_unscaled = pygame.image.load(os.path.join(self.game.assets_dir, "map", "clue_board1.jpg"))
        #self.map_img = pygame.transform.scale(self.map_img_unscaled, (960, 960))
        self.board = [ Tile('Floor1', 'Floor', 150, 0, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor2', 'Floor', 200, 0, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor3', 'Floor', 200, 50, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor4', 'Floor', 150, 50, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor5', 'Floor', 200, 100, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor6', 'Floor', 150, 100, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor7', 'Floor', 150, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor8', 'Floor', 200, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor9', 'Floor', 0, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor10', 'Floor', 50, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor11', 'Floor', 100, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor12', 'Floor', 0, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor13', 'Floor', 50, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor14', 'Floor', 100, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor15', 'Floor', 150, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor16', 'Floor', 200, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor17', 'Floor', 250, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor18', 'Floor', 250, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor19', 'Floor', 300, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor20', 'Floor', 300, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor21', 'Floor', 350, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor22', 'Floor', 350, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor23', 'Floor', 400, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor24', 'Floor', 400, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor25', 'Floor', 450, 150, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor26', 'Floor', 450, 200, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor27', 'Floor', 400, 0, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor28', 'Floor', 450, 0, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor29', 'Floor', 450, 50, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor30', 'Floor', 400, 50, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor31', 'Floor', 400, 100, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor32', 'Floor', 450, 100, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor33', 'Floor', 500, 100, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor34', 'Floor', 500, 150, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor35', 'Floor', 500, 200, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor36', 'Floor', 550, 100, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor37', 'Floor', 550, 150, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor38', 'Floor', 550, 200, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor39', 'Floor', 600, 100, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor40', 'Floor', 600, 150, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor41', 'Floor', 600, 200, 50, 50, (TileFloorColor.get_color())),
                          Tile('Floor42', 'Floor', 450, 250, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor43', 'Floor', 400, 250, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor44', 'Floor', 400, 300, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor45', 'Floor', 450, 300, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor46', 'Floor', 200, 300, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor47', 'Floor', 150, 300, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor48', 'Floor', 200, 250, 50, 50, (TileFloorColor.get_color())),
                      Tile('Floor49', 'Floor', 150, 250, 50, 50, (TileFloorColor.get_color())),

                        Tile('Floor50', 'Floor', 0, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor51', 'Floor', 50, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor52', 'Floor', 100, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor53', 'Floor', 0, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor54', 'Floor', 50, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor55', 'Floor', 100, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor56', 'Floor', 150, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor57', 'Floor', 150, 350, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor58', 'Floor', 150, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor59', 'Floor', 200, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor60', 'Floor', 200, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor61', 'Floor', 200, 350, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor62', 'Floor', 400, 350, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor63', 'Floor', 400, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor64', 'Floor', 400, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor65', 'Floor', 450, 350, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor66', 'Floor', 450, 400, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor67', 'Floor', 450, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor68', 'Floor', 500, 350, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor69', 'Floor', 550, 350, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor70', 'Floor', 600, 350, 50, 50, (TileFloorColor.get_color())),
                      Tile('Wall', 'Wall', 145, 0, 5, 150, (TileWallColor.get_color())),
                      Tile('Wall1', 'Wall', 0, 145, 100, 5, (TileWallColor.get_color())),
                      Tile('Wall2', 'Wall', 250, 0, 5, 150, (TileWallColor.get_color())),
                      Tile('Wall3', 'Wall', 250, 145, 50, 5, (TileWallColor.get_color())),
                      Tile('Wall4', 'Wall', 350, 145, 50, 5, (TileWallColor.get_color())),
                      Tile('Wall5', 'Wall', 400, 0, 5, 150, (TileWallColor.get_color())),
                        Tile('Wall6', 'Wall', 500, 0, 5, 100, (TileWallColor.get_color())),
                        Tile('Wall7', 'Wall', 500, 95, 50, 5, (TileWallColor.get_color())),
                        Tile('Wall8', 'Wall', 550, 95, 50, 5, (TileWallColor.get_color())),
                        Tile('Wall9', 'Wall', 500, 250, 150, 5, (TileWallColor.get_color())),
                        Tile('Wall10', 'Wall', 500, 250, 5, 25, (TileWallColor.get_color())),
                        Tile('Wall11', 'Wall', 500, 325, 5, 25, (TileWallColor.get_color())),
                        Tile('Wall12', 'Wall', 500, 345, 150, 5, (TileWallColor.get_color())),
                        Tile('Wall13', 'Wall', 0, 250, 150, 5, (TileWallColor.get_color())),
                        Tile('Wall14', 'Wall', 145, 250, 5, 50, (TileWallColor.get_color())),
                        Tile('Wall15', 'Wall', 145, 350, 5, 50, (TileWallColor.get_color())),
                        Tile('Wall16', 'Wall', 0, 400, 150, 5, (TileWallColor.get_color())),
                        Tile('Wall17', 'Wall', 500, 400, 5, 50, (TileWallColor.get_color())),
                        Tile('Wall18', 'Wall', 500, 400, 50, 5, (TileWallColor.get_color())),
                        Tile('Wall19', 'Wall', 600, 400, 50, 5, (TileWallColor.get_color())),
                        Tile('Wall20', 'Wall', 500, 500, 5, 50, (TileWallColor.get_color())),
                        Tile('Wall21', 'Wall', 500, 550, 150, 5, (TileWallColor.get_color())),
                      Tile("Kitchen", "Room", 0, 0, 145, 145, (TileRoomColor.get_color())),
                      Tile('Dining Room', 'Room', 255, 0, 145, 145, (TileRoomColor.get_color())),
                        Tile('Conservatory','Room',505,0,150,95,(TileRoomColor.get_color())),
                       Tile('Billiard Room','Room',505,255,150,90,(TileRoomColor.get_color())),
                       Tile('Dining Room','Room',0,255,145,145,(TileRoomColor.get_color())),
                       Tile('Library','Room',505,405,145,145,(TileRoomColor.get_color())),]


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
            if tile.type == 'Floor':
                border_color = BorderColors.get_color()
                border_size = 1
                pygame.draw.rect(screen, border_color, (
                    tile.x + border_size, tile.y + border_size,
                    tile.width - 2 * border_size, tile.height - 2 * border_size)
                                 )

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

    
   




 
