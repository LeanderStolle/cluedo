import pygame, os

from button import *
from states.state import State
from states.game_world import Game_World
from player import PlayerFactory, PlayerColor


class PlayerSelect(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.actions = {"pause": False, "note":False}

        self.img_player_red = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gloria_red_outline.png"))
        self.img_player_yellow = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gatow_red_outline.png"))
        self.img_player_pink = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "orchidee_red_outline.png"))
        self.img_player_green = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gruen_red_outline.png"))
        self.img_player_blue = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "porz_red_outline.png"))
        self.img_player_purple = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "bloom_red_outline.png"))

        self.img_player_red_clicked = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gloria_green_outline.png"))
        self.img_player_yellow_clicked = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gatow_green_outline.png"))
        self.img_player_pink_clicked = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "orchidee_green_outline.png"))
        self.img_player_green_clicked = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "gruen_green_outline.png"))
        self.img_player_blue_clicked = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "porz_green_outline.png"))
        self.img_player_purple_clicked = pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "bloom_green_outline.png"))

        # Create all buttons
        self.player_red_btn = ImgButton(self.game, self.game.SCREEN_WIDTH * 0.25 -51, 100, self.img_player_red, self.img_player_red_clicked, 1, True)
        self.player_yellow_btn = ImgButton(self.game, self.game.SCREEN_WIDTH * 0.5 -51, 100, self.img_player_yellow, self.img_player_yellow_clicked, 1, True)
        self.player_pink_btn = ImgButton(self.game, self.game.SCREEN_WIDTH * 0.75 -51, 100, self.img_player_pink, self.img_player_pink_clicked, 1, True) 
        self.player_green_btn = ImgButton(self.game, self.game.SCREEN_WIDTH * 0.25 -51, 300, self.img_player_green, self.img_player_green_clicked, 1, True)
        self.player_blue_btn = ImgButton(self.game, self.game.SCREEN_WIDTH * 0.5 -51, 300, self.img_player_blue, self.img_player_blue_clicked, 1, True)
        self.player_purple_btn = ImgButton(self.game, self.game.SCREEN_WIDTH * 0.75 -51, 300, self.img_player_purple, self.img_player_purple_clicked, 1, True)


        self.start_btn = Button(self.game, "Start the Game!", self.game.SCREEN_WIDTH/2 - 90 , self.game.SCREEN_HEIGHT/2 + 25, 180, 40, True)


        # Playerstuff
        self.selected_players = []


    def draw_all_player_img(self,screen):
        self.player_red_btn.draw()
        self.player_yellow_btn.draw()
        self.player_pink_btn.draw()
        self.player_green_btn.draw()
        self.player_blue_btn.draw()
        self.player_purple_btn.draw()
    
        

    def update(self, delta_time, actions):
        if self.start_btn.clicked:
            
            if self.player_red_btn.clicked:
                if PlayerColor.RED not in self.selected_players:
                    self.selected_players.append(PlayerColor.RED)
                else:
                    self.selected_players.remove(PlayerColor.RED)

            if self.player_yellow_btn.clicked:
                if PlayerColor.YELLOW not in self.selected_players:
                    self.selected_players.append(PlayerColor.YELLOW)
                else:
                    self.selected_players.remove(PlayerColor.YELLOW)
  

            if self.player_pink_btn.clicked:  
                if PlayerColor.PINK not in self.selected_players:
                    self.selected_players.append(PlayerColor.PINK)
                else:
                    self.selected_players.remove(PlayerColor.PINK)

        
            if self.player_green_btn.clicked:    
                if PlayerColor.GREEN not in self.selected_players:
                    self.selected_players.append(PlayerColor.GREEN)
                else:
                    self.selected_players.remove(PlayerColor.GREEN)

            if self.player_blue_btn.clicked:
                if PlayerColor.BLUE not in self.selected_players:
                    self.selected_players.append(PlayerColor.BLUE)
                else:
                    self.selected_players.remove(PlayerColor.BLUE)

            if self.player_purple_btn.clicked:   
                if PlayerColor.PURPLE not in self.selected_players:
                    self.selected_players.append(PlayerColor.PURPLE)
                else:
                    self.selected_players.remove(PlayerColor.PURPLE)

            if len(self.selected_players) <= 1:
                # TODO add text telling the player to select more players than 1
                pass
            else:
                print( "\n" and self.selected_players)
                print(len(self.selected_players))
                new_state = Game_World(self.game, self.selected_players)
                new_state.enter_state()
        
        
            
        self.game.reset_keys()

    def render(self, screen):
        screen.fill((24, 26, 27))  # Clear the screen
        self.game.draw_title_text(screen, "Choose your Character!", "white", 325, 50)
        self.player_red_btn.draw()
        self.player_yellow_btn.draw()
        self.player_pink_btn.draw()
        self.player_green_btn.draw()
        self.player_blue_btn.draw()
        self.player_purple_btn.draw()
        self.start_btn.draw()
        pygame.display.flip()  # Update the display
        

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)  
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the x, y position of the click
                #Start Button logic
                if self.start_btn.check_click(x, y):
                    self.start_btn.clicked = not self.start_btn.clicked
                #Player Button logic
                if self.player_red_btn.check_click(x, y):
                    self.player_red_btn.clicked = not self.player_red_btn.clicked
                    print("Red",self.player_red_btn.clicked)
                elif self.player_yellow_btn.check_click(x, y):
                    self.player_yellow_btn.clicked = not self.player_yellow_btn.clicked
                    print("yellow",self.player_yellow_btn.clicked)
                elif self.player_pink_btn.check_click(x, y):
                    self.player_pink_btn.clicked = not self.player_pink_btn.clicked
                    print("pink",self.player_pink_btn.clicked)
                elif self.player_green_btn.check_click(x, y):
                    self.player_green_btn.clicked = not self.player_green_btn.clicked
                    print("green",self.player_green_btn.clicked)
                elif self.player_blue_btn.check_click(x, y):
                    self.player_blue_btn.clicked = not self.player_blue_btn.clicked
                    print("blue",self.player_blue_btn.clicked)
                elif self.player_purple_btn.check_click(x, y):
                    self.player_purple_btn.clicked = not self.player_purple_btn.clicked
                    print("purple",self.player_purple_btn.clicked)


