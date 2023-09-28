import pygame, os

from states.state import State
from button import Button

class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)
        self.is_open = False

        #Set the Menu ,Todo: Menu Image Import
        #self.menu_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "#name des Menu images"))
        #self.menu_rect = self.menu_img.get_rect()
        #self.menu_rect.center = (self.game.SCREEN_WIDTH * .8, self.game.SCREEN_HEIGHT * .4)

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
        