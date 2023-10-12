import pygame
import random
from enum import Enum

class PlayerColor(Enum):
    RED = 1
    YELLOW = 2
    PINK = 3
    GREEN = 4
    BLUE = 5
    PURPLE = 6

class PlayerFactory():
    def __init__(self) -> None:
        pass

    def create_player(self, color: PlayerColor):
        if color == PlayerColor.RED:
            return Player("Miss Gloria", PlayerColor.RED, 0, 0)
        if color == PlayerColor.YELLOW:
            return Player("Colonel Mustard", PlayerColor.YELLOW, 0, 0)
        if color == PlayerColor.PINK:
            return Player("Mrs. Orchidee", PlayerColor.PINK, 0, 0)
        if color == PlayerColor.GREEN:
            return Player("Reverend Green", PlayerColor.GREEN, 0, 0)
        if color == PlayerColor.BLUE:
            return Player("Mrs. Porz", PlayerColor.BLUE, 0, 0)
        if color == PlayerColor.PURPLE:
            return Player("Prof. Bloom", PlayerColor.PURPLE, 0, 0)


class Player:
    def __init__(self, name: str, color: PlayerColor, x_pos: int, y_pos:int):
        self.name = name
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.card_list = []

    def add_card_to_stack(self, card):
        self.card_list.append(card)
