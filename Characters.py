import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name, starting_position):
        super().__init__()
        self.image = pygame.Surface((30, 30))  # Placeholder image
        self.rect = self.image.get_rect(center=starting_position)

    def update(self):

        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


