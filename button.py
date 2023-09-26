import pygame




class Button:
    def __init__(self, game, text, x_pos, y_pos, width, height, enabled):
        self.game = game
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.width = width
        self.height = height
        self.button_text = self.game.font.render(self.text, True, "black")
        self.button_rect = pygame.rect.Rect((self.x_pos,self.y_pos), (self.width,self.height))
        self.new_press = True
        


    def draw(self):
        if self.check_click():
            pygame.draw.rect(self.game.screen, "dark gray", self.button_rect, 0, 5)
        else:
            pygame.draw.rect(self.game.screen, "light gray", self.button_rect, 0, 5)

        pygame.draw.rect(self.game.screen, "black", self.button_rect, 2, 5)
        self.game.screen.blit(self.button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos), (self.width,self.height))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
