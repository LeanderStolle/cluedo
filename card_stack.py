import pygame, random
import Weapon
import Characters
import Room


class CardStack:
    def __init__(self, cards):
        self.cards = cards

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return "No more cards in the stack"
    
    def shuffle_cards(self):
        random.shuffle(self.cards)

    def __add__(self, other):
        self.cards.append(other)
        return self

weapon_cardstack = CardStack([Weapon.Seil, Weapon.Dolch, Weapon.Pistole, Weapon.Heizungsrohr, Weapon.Rohrzange, Weapon.Kerzenständer])
character_cardstack = CardStack([Characters.Miss_Scarlett, Characters.Colonel_Mustard, Characters.Mrs_White, Characters.Mr_Green, Characters.Mrs_Peacock, Characters.Professor_Plum])
room_cardstack = CardStack([Room.Ballroom, Room.Billiard_Room, Room.Conservatory, Room.Dining_Room, Room.Hall, Room.Kitchen, Room.Library, Room.Lounge, Room.Study])