import pygame, os

from button import Button
from states.state import State
from states.game_world import Game_World



class CharacterSelect(State):
    def __init__(self, game):
        State.__init__(self, game)


        self.character_images = [
            pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "frl_gloria.png")), #rot  
            pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "oberst_gatow.png")), #gelb
            pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "dr_orchidee.png")), #pink
            pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "rev_gruen.png")), #grün
            pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "baronin_porz.png")), #blau
            pygame.image.load(os.path.join(self.game.assets_dir, "sprites", "prof_bloom.png"))  #lila
        ]

        self.character_positions = [(100, 100), (300, 100), (500, 100), (100, 300), (300, 300), (500, 300)] #alle 102x120 px groß

        self.selected_characters = []


        self.start_btn = Button(self.game, "Start the Game!", self.game.SCREEN_WIDTH/2 - 75 , self.game.SCREEN_HEIGHT/2 + 25, 200, 40, True)

    def draw_characters(self,screen):
        for i, image in enumerate(self.character_images):
            x, y = self.character_positions[i]
            screen.blit(image, (x, y))   
    
        

    def update(self, delta_time, actions):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, (char_x, char_y) in enumerate(self.character_positions):
                    if char_x < x < char_x + self.character_images[i].get_width() and char_y < y < char_y + self.character_images[i].get_height():
                        # Character clicked, toggle selection
                        if i in self.selected_characters:
                            self.selected_characters.remove(i)
                            print("Spieler wurde entfernt")
                        else:
                            self.selected_characters.append(i)
                            print("spieler hinzugefügt")
        
        if pygame.mouse.get_pressed()[0] and self.start_btn.new_press:
            self.start_btn.new_press = False
            if self.start_btn.check_click:
                print("buttton clicked")
                new_state = Game_World(self.game)
                new_state.enter_state()
        if not pygame.mouse.get_pressed()[0] and not self.start_btn.new_press:
            self.start_btn.new_press = True

        self.game.reset_keys()

    def render(self, screen):
        screen.fill((255, 255, 255))  # Clear the screen
        self.draw_characters(screen)  # Draw character images
        self.start_btn.draw()
        pygame.display.flip()  # Update the display
        

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.actions["pause"] = True  
                if event.key == pygame.K_SPACE:
                    self.actions["note"] = True   