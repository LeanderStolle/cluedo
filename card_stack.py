import pygame, random


class CardStack:
    def __init__(self):
        self.cards = ["Card 1", "Card 2", "Card 3", "Card 4", "Card 5"]

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return "No more cards in the stack"
    
    def shuffle_cards(self):
        random.shuffle(self.cards)