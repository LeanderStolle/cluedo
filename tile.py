import pygame

class Tile:
    def __init__(self, name, type, x, y, width, height, color):
        self.name = name
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color



    def contains_point(self, x, y):
        if x >= self.x and x <= self.x + self.width:
            if y >= self.y and y <= self.y + self.height:
                return True
        return False
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_pos(self):
        return (self.x, self.y)

    def get_size(self):
        return (self.width, self.height)

    def get_center(self):
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2
        return center_x,center_y

    def get_color(self):
        return self.color
    def get_name(self):
        return self.name