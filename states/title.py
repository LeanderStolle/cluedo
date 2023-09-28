import pygame
from states.state import State
from states.game_world import Game_World
from button import Button


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)

        self.play_btn = Button(self.game, "Play", self.game.SCREEN_WIDTH/2 - 75 , self.game.SCREEN_HEIGHT/2 + 25, 150, 40, True)
        self.options_btn = Button(self.game, "Options", self.game.SCREEN_WIDTH/2 - 75, self.game.SCREEN_HEIGHT/2 + 70, 150, 40, True)
    
    def update(self, delta_time, actions):
        # Logik des Play Buttons
        if pygame.mouse.get_pressed()[0] and self.play_btn.new_press:
            self.play_btn.new_press = False
            if self.play_btn.check_click:
                new_state = Game_World(self.game)
                new_state.enter_state()
        if not pygame.mouse.get_pressed()[0] and not self.play_btn.new_press:
            self.play_btn.new_press = True
        
        self.game.reset_keys()

    def render(self, screen):
        screen.fill((255,255,255))
        self.game.draw_title_text(screen, "Cluedo", (0,0,0), self.game.SCREEN_WIDTH/2, self.game.SCREEN_HEIGHT/2 - 200)
        self.play_btn.draw()
        self.options_btn.draw()

        
