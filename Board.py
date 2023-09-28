import pygame

from Tile import Tile

class Board:
    def __init__(self):
        self.board = [Tile.Tile("Kitchen", "Room", 0, 0, 150, 150, (255,248,220)),Tile.Tile('Wall', 'wall', 150, 0, 50, 150, (0,0,0))]

    def draw_board(self, screen):
        for row in range(len(self.cluedo_board)):
            tile = self.cluedo_board[row]
            pygame.draw.rect(screen,tile.color, (tile.x, tile.y, tile.width, tile.height))




