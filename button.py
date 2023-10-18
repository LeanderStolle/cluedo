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
        
        self.clicked = False
        self.new_press = True
        self.handled = False
        


    def draw(self):
        pygame.draw.rect(self.game.screen, "light gray", self.button_rect, 0, 5)
        pygame.draw.rect(self.game.screen, "black", self.button_rect, 2, 5)
        self.game.screen.blit(self.button_text, self.button_text.get_rect(center = self.button_rect.center))

    def check_click(self, x, y):
        mouse_pos = (x, y)
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos), (self.width,self.height))
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False



class ImgButton:
    def __init__(self, game, x_pos, y_pos, image, click_image, scale, enabled):
        self.game = game
        self.clicked = False
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = image.get_width()
        self.height = image.get_height()
        self.original_image = image
        self.click_image = click_image
        self.image = self.original_image
        #self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.button_rect = self.image.get_rect()
        self.button_rect.topleft = (x_pos, y_pos)
        self.enabled = enabled

    def draw(self):
        self.image = self.click_image if self.clicked else self.original_image
        self.game.screen.blit(self.image, (self.button_rect.x, self.button_rect.y))

    def check_click(self, x, y):
        mouse_pos = (x, y)
        if self.button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
            