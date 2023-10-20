import pygame
import random
from enum import Enum

import colors
from colors import *
from tile import *
from states.game_world import *
from card import *
from board import *
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
            return Player("Miss Gloria", PlayerColor.RED, colors.Red.get_color(), "Floor41",1)
        if color == PlayerColor.YELLOW:
            return Player("Colonel Mustard", PlayerColor.YELLOW, colors.Yellow.get_color(),"Floor87",2)
        if color == PlayerColor.PINK:
            return Player("Mrs. Orchidee", PlayerColor.PINK, colors.Pink.get_color(), "Floor27",3)
        if color == PlayerColor.GREEN:
            return Player("Reverend Green", PlayerColor.GREEN, colors.Green.get_color(), "Floor97",4)
        if color == PlayerColor.BLUE:
            return Player("Mrs. Porz", PlayerColor.BLUE, colors.Blue.get_color(), "Floor9",5)
        if color == PlayerColor.PURPLE:
            return Player("Prof. Bloom", PlayerColor.PURPLE, colors.Purple.get_color(), "Floor106",6)



class Player:
    def __init__(self, name: str, color: PlayerColor,rgb, tile,turn_number):
        self.name = name
        self.color = color
        self.rgb = rgb
        self.tile = tile
        self.card_list = []
        self.turn_number = turn_number
        self.move = True
        self.suspect = True
        self.playing = True

    def add_card(self, card):
        self.card_list.append(card)

    def get_name(self):
        return self.name
