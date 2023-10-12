# Regeln hinzufügen
#


import pygame, os

from states.state import State
from button import Button

class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)

        self.actions = {"pause": False}

        self.is_open = False

        # Initialisiere Buttons
        self.exit_btn = Button(self.game, "Exit", self.game.SCREEN_WIDTH/2 - 75 , self.game.SCREEN_HEIGHT/2 + 25, 150, 40, True)


    def update(self, delta_time, actions):
        if actions["pause"] and self.is_open:
            self.is_open = False
            self.exit_state()
        if self.exit_btn.clicked:
            exit(0)    
        


    def render(self, screen):
        self.prev_state.render(screen)
        screen.fill((255,255,255))
        self.game.draw_title_text(screen, "-Paused-", (0,0,0), self.game.SCREEN_WIDTH/2, self.game.SCREEN_HEIGHT/2 - 200)
        self.exit_btn.draw()
        

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["pause"] = True 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the x, y position of the click
                if self.exit_btn.check_click(x, y):
                    self.exit_btn.clicked = not self.exit_btn.clicked  