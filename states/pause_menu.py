# Regeln hinzufügen
#


import pygame, os

from states.state import State
from button import Button

class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)
        self.is_open = False

        # Initialisiere Buttons
        self.exit_btn = Button(self.game, "Exit", self.game.SCREEN_WIDTH/2 - 75 , self.game.SCREEN_HEIGHT/2 + 25, 150, 40, True)


    def update(self, delta_time, actions):
        if actions["pause"] and self.is_open:
            self.is_open = False
            self.exit_state()
        self.game.reset_keys()

        #Logic of the exit button
        if pygame.mouse.get_pressed()[0] and self.exit_btn.new_press:
            self.exit_btn.new_press = False
            if self.exit_btn.check_click:
                self.running, self.playing = False, False
        if not pygame.mouse.get_pressed()[0] and not self.exit_btn.new_press:
            self.exit_btn.new_press = True

    def render(self, screen):
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
                if event.key == pygame.K_SPACE:
                    self.actions["note"] = True  