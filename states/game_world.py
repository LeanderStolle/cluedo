import pygame, os

from states.state import State
from states.pause_menu import PauseMenu
from states.note import Note
from Tile import Tile
from colors import *
from player import PlayerFactory

class Game_World(State):
    def __init__(self, game, selected_players):
        State.__init__(self, game)
        

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
                        Tile('Floor71', 'Floor', 350, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor72', 'Floor', 300, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor73', 'Floor', 250, 450, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor74', 'Floor', 350, 500, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor75', 'Floor', 350, 550, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor76', 'Floor', 400, 500, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor77', 'Floor', 400, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor77', 'Floor', 300, 500, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor78', 'Floor', 300, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor79', 'Floor', 250, 500, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor80', 'Floor', 250, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor81', 'Floor', 450, 500, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor82', 'Floor', 450, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor83', 'Floor', 200, 500, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor84', 'Floor', 200, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor85', 'Floor', 500, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor86', 'Floor', 550, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor87', 'Floor', 600, 550, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor88', 'Floor', 500, 600, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor89', 'Floor', 550, 600, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor90', 'Floor', 600, 600, 50, 50, (TileFloorColor.get_color())),
                          Tile('Floor91', 'Floor', 450, 650, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor92', 'Floor', 400, 650, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor93', 'Floor', 400, 600, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor94', 'Floor', 450, 600, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor95', 'Floor', 400, 700, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor96', 'Floor', 450, 700, 50, 50, (TileFloorColor.get_color())),
                       Tile('Floor97', 'Floor', 0, 500, 50, 50, (TileFloorColor.get_color())),
                          Tile('Floor98', 'Floor', 50, 500, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor99', 'Floor', 100, 500, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor100', 'Floor', 150, 500, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor101', 'Floor', 150, 600, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor102', 'Floor', 150, 650, 50, 50, (TileFloorColor.get_color())),
                          Tile('Floor103', 'Floor', 200, 600, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor104', 'Floor', 200, 650, 50, 50, (TileFloorColor.get_color())),
                            Tile('Floor105', 'Floor', 150, 550, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor106', 'Floor', 150, 700, 50, 50, (TileFloorColor.get_color())),
                        Tile('Floor107', 'Floor', 200, 700, 50, 50, (TileFloorColor.get_color())),
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
                        Tile('Wall22', 'Wall', 550, 650, 100, 5, (TileWallColor.get_color())),
                        Tile('Wall23', 'Wall', 500, 650, 5, 100, (TileWallColor.get_color())),
                        Tile('Wall24', 'Wall', 400, 600, 5, 150, (TileWallColor.get_color())),
                        Tile('Wall25', 'Wall', 350, 600, 50, 5, (TileWallColor.get_color())),
                        Tile('Wall26', 'Wall', 250, 600, 50, 5, (TileWallColor.get_color())),
                        Tile('Wall27', 'Wall', 250, 600, 5, 150, (TileWallColor.get_color())),
                        Tile('Wall28', 'Wall', 0, 550, 100, 5, (TileWallColor.get_color())),
                        Tile('Wall29', 'Wall', 145, 550, 5, 200, (TileWallColor.get_color())),
                      Tile("Kitchen", "Room", 0, 0, 145, 145, (TileRoomColor.get_color())),
                      Tile('Dining Room', 'Room', 255, 0, 145, 145, (TileRoomColor.get_color())),
                        Tile('Conservatory','Room',505,0,150,95,(TileRoomColor.get_color())),
                       Tile('Billiard Room','Room',505,255,150,90,(TileRoomColor.get_color())),
                       Tile('Dining Room','Room',0,255,145,145,(TileRoomColor.get_color())),
                       Tile('Library','Room',505,405,145,145,(TileRoomColor.get_color())),
                       Tile('Study','Room',505,655,145,95,(TileRoomColor.get_color())),
                          Tile('Hall','Room',255,605,145,145,(TileRoomColor.get_color())),
                            Tile('Lounge','Room',0,555,145,195,(TileRoomColor.get_color())),
                       ]
        # Definiere Actions
        self.actions = {"pause": False, "note":False}

        self.selected_players = selected_players
        
        tmp_list = []
        factory = PlayerFactory()
        for elem in self.selected_players:
            tmp_list.append(factory.create_player(elem))

        # Override selected players list containing color codes with actual object based on colors
        self.selected_players = tmp_list

    def get_neighbours(self, given_tile):
        neighbours = []
        for tile in self.board:
            if tile.type == 'Wall' or tile.name == given_tile.name:
                continue  #Überspringe wall tile und das übergebene tile

            # überprüfen ob tiles horizontal  benachbart sind
            if (given_tile.y < tile.y + tile.height) and (tile.y < given_tile.y + given_tile.height):
                # 5px abstand zwischen Floor und Room tiles
                gap = 5 if (tile.type == 'Room' or given_tile.type == 'Room') else 0
                # Wenn der horizontale Abstand zwischen den Mittelpunkten zweier Tiles
                # kleiner oder gleich der Summe der Hälfte ihrer Breiten und der Lücke ist,
                # werden sie als benachbart betrachtet.
                if abs((tile.x + tile.width / 2) - (given_tile.x + given_tile.width / 2)) <= (
                        tile.width + given_tile.width) / 2 + gap:
                    neighbours.append(tile)
                    continue


            if (given_tile.x < tile.x + tile.width) and (tile.x < given_tile.x + given_tile.width):
                gap = 5 if (tile.type == 'Room' or given_tile.type == 'Room') else 0
                if abs((tile.y + tile.height / 2) - (given_tile.y + given_tile.height / 2)) <= (
                        tile.height + given_tile.height) / 2 + gap:
                    neighbours.append(tile)

        return neighbours

    def find_possible_moves(self, tile, steps):
        possible_moves = set()
        current_tiles = [tile]
        for _ in range(steps):
            next_tiles = []
            for t in current_tiles:
                neighbours = self.get_neighbours(t)
                for neighbour in neighbours:
                    if neighbour not in possible_moves:
                        possible_moves.add(neighbour)
                        next_tiles.append(neighbour)
            current_tiles = next_tiles
        return list(possible_moves)

    def tile_get_name_from_coordinates(self, x, y):
        for tile in self.board:
            if tile.x <= x < tile.x + tile.width and tile.y <= y < tile.y + tile.height:
                return tile.name
        return None

    def find_tile_at_position(self, x, y):
        for tile in self.board:
            if tile.x <= x < tile.x + tile.width and tile.y <= y < tile.y + tile.height:
                return tile
        return None

    def find_tile_by_name(self, name):
        for tile in self.board:
            if tile.name == name:
                print(tile.name)
                return tile
        return None

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
        screen.fill((255,255,255))
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
                    tile.width - 2 * border_size, tile.height - 2 * border_size))
            # Render room name
            if tile.type == 'Room':
                font = pygame.font.Font(None, 24)  # Adjust the font size as needed
                text = font.render(tile.name, True, (0, 0, 0))  # Text color: (0, 0, 0) is black
                text_rect = text.get_rect(center=(tile.x + tile.width // 2, tile.y + tile.height // 2))
                screen.blit(text, text_rect)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["pause"] = True  
                if event.key == pygame.K_SPACE:
                    self.actions["note"] = True   
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the x, y position of the click
                if self.find_tile_at_position(x,y) in self.board:
                    print(self.find_tile_at_position(x,y).name)

#TO-DO:
#  1. Alle Spielfiguren platzieren
#  2. Waffen platzieren
#  3. 29 Beweisarten initialisieren und auf dem Board platzieren (Beweiskarten maybe Optional)
#  4. übrige Karten auf Stapel aufteilen ( Personen, Waffen, Räume), dann mischen und auch verdeckt platzieren
#  5. von jedem Stapel (Personen, Waffe, Räume) muss eine Karte in die Fallakte (Lösung)
#  6. Mischen der übrigen Karten und verteilen an Spieler (nicht schlimm wenn jemand mehr Karten hat als der andere)
#  7. Spielstart --> möglichkeit seine Beweiskarten anzuschauen (im eigenen Spielzug)
#  
# Allgemeines:
# - maybe ein Turnhandler? damit
# - maybe UI mit aktivem Spielernamen, Buttons fürs Würfel, anschuldigen, karten anschauen, notes taken
#
# actions für jeden State definieren und in game.py bei update die actions für jeden State mitgeben

