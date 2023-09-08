import pygame
import pygame_menu


class MainMenu:
    def __init__(self, game):
        self.game = game
        self.menu = pygame_menu.Menu(
            height=400,
            width=600,
            theme=pygame_menu.themes.THEME_DARK,
            title='Cluedo Main Menu',
        )

        # menu items
        self.menu.add.button('Play', self.start_game)
        self.menu.add.button('Options', self.open_options)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def start_game(self):
        self.game.switch_to_gameplay()

    def open_options(self):#falls wir optionen einbauen werden diese hier eingebaut
        pass

    def run(self, screen):
        # startet mainloop für optionen ist eine funktion aus pygame_menu
        self.menu.mainloop(screen)