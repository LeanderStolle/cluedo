import pygame, os

from states.state import State

class Note(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)
        self.is_open = False

        #Set the Note ,Todo: Menu Image Import
        self.note_img = pygame.image.load(os.path.join(self.game.assets_dir, "note", "cluedo_note.jpg"))
        self.note_rect = self.note_img.get_rect()
        self.note_rect.center = (self.game.SCREEN_WIDTH * .8, self.game.SCREEN_HEIGHT * .4)


    def update(self, delta_time, actions):
        if actions["note"] and self.is_open:
            self.is_open = False
            self.exit_state()
        self.game.reset_keys()

    def render(self, screen):
        self.prev_state.render(screen)
        screen.blit(self.note_img, self.note_rect)