import pygame, os
from states.state import State

from states.player_select import PlayerSelect
from button import Button


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.actions = {"pause": False, "note":False}

        
        self.logo_img = pygame.image.load(os.path.join(self.game.assets_dir, "logo", "cluedo_logo.png"))
        self.width = self.logo_img.get_width()
        self.height = self.logo_img.get_height()
        self.logo_scaled = pygame.transform.scale(self.logo_img, (int(self.width * .8), int(self.height * .8)))
        self.logo_rect = self.logo_img.get_rect()
        self.logo_rect.center = (self.game.SCREEN_WIDTH/2 + 50, self.game.SCREEN_HEIGHT/2 - 200)
        
        self.play_btn = Button(self.game, "Play", self.game.SCREEN_WIDTH/2 - 75 , self.game.SCREEN_HEIGHT/2 + 25, 150, 40, True)
    
    def update(self, delta_time, actions):
        # Logik des Play Buttons
        if self.play_btn.clicked:
            new_state = PlayerSelect(self.game)
            new_state.enter_state()
        
        self.game.reset_keys()

    def render(self, screen):
        screen.fill((255,255,255))
        screen.blit(self.logo_scaled, self.logo_rect)
        self.play_btn.draw()
        

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the x, y position of the click
                if self.play_btn.check_click(x, y):
                    self.play_btn.clicked = not self.play_btn.clicked
                   
        
