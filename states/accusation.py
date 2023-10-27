import sys
from button import *
from states.state import State
from card_stack import *
from board import *
from tile import *


class Accusation(State):
    def __init__(self, game,active_players, current_player):
        State.__init__(self, game)

        #Definiere Actions
        self.actions = {"pause": False, "note":False}
        self.active_players = active_players
        self.current_player = current_player

        self.list = [  Tile('Rope', 'Weapon', 15, 0, 200, 90, (TileWeaponColor.get_color())),
                       Tile('Wrench', 'Weapon', 225, 0, 200, 90, (TileWeaponColor.get_color())),
                       Tile('Revolver', 'Weapon', 435, 0, 200, 90, (TileWeaponColor.get_color())),
                       Tile('Knife', 'Weapon', 15, 105, 200 ,90, (TileWeaponColor.get_color())),
                       Tile('Candlestick', 'Weapon', 225, 105, 200, 90, (TileWeaponColor.get_color())),
                       Tile('Lead Pipe', 'Weapon', 435, 105, 200, 90, (TileWeaponColor.get_color())),
                       Tile('Miss Scarlett', 'Character', 15, 210, 200, 90, (TileCharacterColor.get_color())),
                       Tile('Colonel Mustard', 'Character', 225, 210, 200, 90, (TileCharacterColor.get_color())),
                       Tile('Mrs. White', 'Character', 435, 210, 200, 90, (TileCharacterColor.get_color())),
                       Tile('Mr. Green', 'Character', 15, 315, 200, 90, (TileCharacterColor.get_color())),
                       Tile('Mrs. Peacock', 'Character', 225, 315, 200, 90, (TileCharacterColor.get_color())),
                       Tile('Professor Plum', 'Character', 435, 315, 200, 90, (TileCharacterColor.get_color())),
                       Tile("Kitchen", "Room", 15, 420, 200, 90, (TileRoomColor.get_color())),
                       Tile('Ball Room', 'Room', 225, 420, 200, 90, (TileRoomColor.get_color())),
                       Tile('Conservatory', 'Room', 435, 420, 200, 90, (TileRoomColor.get_color())),
                       Tile('Billiard Room', 'Room', 15, 525, 200, 90, (TileRoomColor.get_color())),
                       Tile('Dining Room', 'Room', 225, 525, 200, 90, (TileRoomColor.get_color())),
                       Tile('Library', 'Room', 435, 525, 200, 90, (TileRoomColor.get_color())),
                       Tile('Study', 'Room', 15, 630, 200, 90, (TileRoomColor.get_color())),
                       Tile('Hall', 'Room', 225, 630, 200, 90, (TileRoomColor.get_color())),
                       Tile('Lounge', 'Room', 435, 630, 200, 90, (TileRoomColor.get_color()))]

        self.Accuse_btn = Button(self.game, "Accuse", 250, 850, 150, 40, True)
        self.Back_btn = Button(self.game, "Back", 250, 900, 150, 40, True)
        self.Back_btn_Popup = Button(self.game, "Back", 250, 600, 150, 40, True)
        self.accusation = []
        self.suspicionv = False
        self.Weapon_count = 0
        self.Character_count = 0
        self.Room_count = 0
        self.board = Board()
        self.gameover = False

        self.case_file = [Case_File[0].name, Case_File[1].name, Case_File[2].name]
        print(self.case_file)


    def check_accusation(self):
        sorted_arr1 = sorted(self.accusation)
        sorted_arr2 = sorted(self.case_file)
        if sorted_arr1 == sorted_arr2:
            return True
        else:
            return False


    def show_popup(self,screen):
        if self.suspicionv==True:
            font = pygame.font.Font(None, 24)
            popup_width, popup_height = 350, 450
            border_size = 5  # Border size in pixels

            # Calculate the position and size of the popup
            popup_rect = pygame.Rect((650 - popup_width) // 2, (960 - popup_height) // 2, popup_width,
                                     popup_height)

            # Draw background
            pygame.draw.rect(screen, (200, 200, 200), popup_rect)

            # Draw border around the background
            pygame.draw.rect(screen, (0, 0, 0), popup_rect, border_size)
            self.Back_btn_Popup.draw()

            if self.check_accusation() == True:
                text_surface = font.render("Sie haben gewonnnen", True, (0, 0, 0))
                self.gameover = True
                text_rect = text_surface.get_rect(center=popup_rect.center)
                screen.blit(text_surface, text_rect)

            else:
                text_surface = font.render("Du bist raus (Exmatrikulation ist auch raus)", True, (0, 0, 0))
                self.current_player.playing = False
                text_rect = text_surface.get_rect(center=popup_rect.center)
                screen.blit(text_surface, text_rect)

            pygame.display.flip()

    def draw_list(self, screen):
            for row in range(len(self.list)):
                tile = self.list[row]
                pygame.draw.rect(screen, tile.color, (tile.x, tile.y, tile.width, tile.height))
                font = pygame.font.Font(None, 24) 
                text = font.render(tile.name, True, (0, 0, 0)) 
                text_rect = text.get_rect(center=(tile.x + tile.width // 2, tile.y + tile.height // 2))
                screen.blit(text, text_rect)

                if tile.clicked:
                    border_size = 5
                    border_color = (255, 0, 0)  # Green
                    pygame.draw.rect(screen, border_color, (tile.x, tile.y, tile.width, border_size))
                    # Draw bottom border
                    pygame.draw.rect(screen, border_color,
                                     (tile.x, tile.y + tile.height - border_size, tile.width, border_size))
                    # Draw left border
                    pygame.draw.rect(screen, border_color, (tile.x, tile.y, border_size, tile.height))
                    # Draw right border
                    pygame.draw.rect(screen, border_color,
                                     (tile.x + tile.width - border_size, tile.y, border_size, tile.height))

    def find_tile_at_position(self, x, y):
        for tile in self.list:
            if tile.x <= x < tile.x + tile.width and tile.y <= y < tile.y + tile.height:
                return tile
        return None

    def update(self, delta_time, actions):
        if self.Accuse_btn.clicked:
            for tile in self.list:
                if tile.clicked:
                    self.accusation.append(tile.name)
                    print(self.accusation)
            self.suspicionv = True
            self.Accuse_btn.clicked = False
        if self.Back_btn.clicked:
                self.game.state_stack.pop()
                self.Back_btn.clicked = False
        if self.Back_btn_Popup.clicked:
            if self.gameover == True:
                sys.exit()
            self.suspicionv = False
            self.Back_btn_Popup = False
            self.current_player.suspect = False
            self.current_player.move = False
            self.game.state_stack.pop()


    def render(self, screen):
        screen.fill((24, 26, 27))  # Clear the screen
        self.draw_list(screen)
        self.Accuse_btn.draw()
        self.Back_btn.draw()
        self.show_popup(screen)
        pygame.display.flip()  # Update the display

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the x, y position of the click
                if self.find_tile_at_position(x, y) in self.list and self.find_tile_at_position(x, y).type == 'Weapon' and self.Weapon_count == 0 :
                        self.find_tile_at_position(x, y).clicked = True
                        self.Weapon_count = 1
                elif self.find_tile_at_position(x, y) in self.list and self.find_tile_at_position(x, y).type == 'Weapon' and self.Weapon_count == 1 and self.find_tile_at_position(x, y).clicked == True:
                    self.find_tile_at_position(x, y).clicked = False
                    self.Weapon_count = 0
                elif self.find_tile_at_position(x, y) in self.list and self.find_tile_at_position(x, y).type == 'Character' and self.Character_count == 1 and self.find_tile_at_position(x, y).clicked == True:
                        self.find_tile_at_position(x, y).clicked = False
                        self.Character_count = 0
                elif self.find_tile_at_position(x, y) in self.list and self.find_tile_at_position(x, y).type == 'Character' and self.Character_count == 0:
                        self.find_tile_at_position(x, y).clicked = True
                        self.Character_count = 1
                elif self.find_tile_at_position(x, y) in self.list and self.find_tile_at_position(x, y).type == 'Room' and self.Room_count == 1 and self.find_tile_at_position(x, y).clicked == True:
                        self.find_tile_at_position(x, y).clicked = False
                        self.Room_count = 0
                elif self.find_tile_at_position(x, y) in self.list and self.find_tile_at_position(x, y).type == 'Room' and self.Room_count == 0:
                        self.find_tile_at_position(x, y).clicked = True
                        self.Room_count = 1
                if self.Accuse_btn.check_click(x,y):
                    self.Accuse_btn.clicked = not self.Accuse_btn.clicked
                if self.Back_btn.check_click(x,y):
                    self.Back_btn.clicked = not self.Back_btn.clicked
                if self.Back_btn_Popup.check_click(x,y):
                    self.Back_btn_Popup.clicked = not self.Back_btn_Popup.clicked
