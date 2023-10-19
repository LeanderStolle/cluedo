import pygame, random
import weapon

from card import *


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
        # Create a new instance of CardStack with combined cards
        return CardStack(self.cards + other.cards)
    def __len__(self):
        return len(self.cards)

weapon_cardstack = CardStack([Rope_Card, Wrench_Card, Revolver_Card, Knife_Card, Candlestick_Card, Lead_Pipe_Card])
character_cardstack = CardStack([Miss_Scarlett_Card, Colonel_Mustard_Card, Mrs_White_Card, Mr_Green_Card, Mrs_Peacock_Card, Professor_Plum_Card])
room_cardstack = CardStack([Kitchen_Card, Ballroom_Card, Conservatory_Card, Dining_Room_Card, Billiard_Room_Card, Library_Card, Lounge_Card, Hall_Card, Study_Card])

Case_File = [weapon_cardstack.draw_card(), character_cardstack.draw_card(), room_cardstack.draw_card()]

combined_cardstack = weapon_cardstack + (room_cardstack + character_cardstack)

combined_cardstack.shuffle_cards()

drawn_card =combined_cardstack.draw_card()
print([card.get_name() for card in Case_File])
print(drawn_card.get_name())