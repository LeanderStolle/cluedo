# checken ob ein Spieler einen Raum betreten hat oder in einem Raum steht
# man verdächtigt immer den Raum in dem man steht, eine Waffe und eine Person
# bewege den verdächtigten Spieler + Tatwaffe in den Raum
# der Spieler Links neben dir zeigt dir nun EINE verdächtigte Karte solange er sie besitzt, bei mehreren nur eine zeigen
# wenn der Spieler links von dir keine dieser Karten hat geht es im Uhrzeigersinn weiter, sobald eine Karte gezeigt wurde endet die Befragung
#
# --> accusation state
# --> note state
import os
from button import *
from states.state import State
from tile import *
from colors import *
import pygame


class Suspicion(State):
    def __init__(self, game):
        State.__init__(self, game)

        #Definiere Actions
        self.actions = {"pause": False, "note":False}

        self.img_player_red = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gloria_red_outline.png"))
        self.img_player_yellow = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gatow_red_outline.png"))
        self.img_player_pink = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "orchidee_red_outline.png"))
        self.img_player_green = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gruen_red_outline.png"))
        self.img_player_blue = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "porz_red_outline.png"))
        self.img_player_purple = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "bloom_red_outline.png"))

        self.list = [  Tile('Rope', 'Weapon', 15, 0, 200, 200, (TileWeaponColor.get_color())),
                       Tile('Wrench', 'Weapon', 225, 0, 200, 200, (TileWeaponColor.get_color())),
                       Tile('Revolver', 'Weapon', 435, 0, 200, 200, (TileWeaponColor.get_color())),
                       Tile('Knife', 'Weapon', 15, 210, 200, 200, (TileWeaponColor.get_color())),
                       Tile('Candlestick', 'Weapon', 225, 210, 200, 200, (TileWeaponColor.get_color())),
                       Tile('Lead Pipe', 'Weapon', 435, 210, 200, 200, (TileWeaponColor.get_color())),
                       Tile('Miss Scarlett', 'Character', 15, 420, 200, 200, (TileCharacterColor.get_color())),
                       Tile('Colonel Mustard', 'Character', 225, 420, 200, 200, (TileCharacterColor.get_color())),
                       Tile('Mrs. White', 'Character', 435, 420, 200, 200, (TileCharacterColor.get_color())),
                       Tile('Mr. Green', 'Character', 15, 640, 200, 200, (TileCharacterColor.get_color())),
                       Tile('Mrs. Peacock', 'Character', 225, 640, 200, 200, (TileCharacterColor.get_color())),
                       Tile('Professor Plum', 'Character', 435, 640, 200, 200, (TileCharacterColor.get_color()))]

        self.Weapon_count = 0
        self.Character_count = 0

        self.Suspect_btn = Button(self.game, "Suspect", 0, 700, 150, 40, True)

    def draw_list(self, screen):
            for row in range(len(self.list)):
                tile = self.list[row]
                pygame.draw.rect(screen, tile.color, (tile.x, tile.y, tile.width, tile.height))
                font = pygame.font.Font(None, 24)  # Adjust the font size as needed
                text = font.render(tile.name, True, (0, 0, 0))  # Text color: (0, 0, 0) is black
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
        if self.Suspect_btn.clicked:
            self.game.state_stack.pop()


    def render(self, screen):
        screen.fill((255, 255, 255))  # Clear the screen
        self.draw_list(screen)
        self.Suspect_btn.draw()
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
                if self.Suspect_btn.check_click(x,y):
                    self.Suspect_btn.clicked = not self.Suspect_btn.clicked


