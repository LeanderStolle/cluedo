import os, time, pygame

from states.title import Title


class Game():
    def __init__(self):
        pygame.init()
        #Displayvariablen festlegen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 650, 960
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Cluedo a Detective Game!")
        self.fps = 60
        self.timer = pygame.time.Clock()


        #Definiere ob das Spiel läuft
        self.running, self.playing = True, True

        #Definiere Actions
        self.actions = {"pause": False, "note":False}

        #Dotted Time Variablen
        
        self.dt, self.prev_time = 0, 0 

        #State Stack
        self.state_stack = []

        #Laden der Assets/states
        self.load_assets()
        self.load_states()


    def game_loop(self):
        while self.playing:

            self.timer.tick(self.fps)
            self.get_events()
            self.update()
            self.render()


    def get_events(self):
        self.state_stack[-1].get_events()

                
    def reset_keys(self):
        self.actions["pause"] = False
        self.actions["note"] = False

    def update(self):
        #Führt die Update Funktion für das letzte Objekt im State_Stack aus
        self.state_stack[-1].update(self.dt, self.state_stack[-1].actions)

    def render(self):
        self.state_stack[-1].render(self.screen)
        self.screen.blit(pygame.transform.scale(self.screen,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def draw_title_text(self, surface, text, color, x, y):
        text_surface = self.title_font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        #Erstelle die Referenz zu den directories
        self.game_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.game_dir, "assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.title_font = pygame.font.Font(os.path.join(self.font_dir, "Absortile-Bold.ttf"), 40)
        self.font = pygame.font.Font(os.path.join(self.font_dir, "Absortile.ttf"), 24)
        self.small_font = pygame.font.Font(os.path.join(self.font_dir, "Absortile.ttf"), 16)

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)


# not you can start the game from the game class
if __name__ == "__main__":

    g = Game()

    while g.running:
        g.game_loop()


    

    