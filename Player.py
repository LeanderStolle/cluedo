import pygame
from character import Character


class Player(pygame.sprite.Sprite):
    players = []

    def __init__(self, character):
        super().__init__()
        self.turn_number = len(Player.players) + 1 
        Player.players.append(self)
        self.character = character
        # self.start_position = start_position
