import random
from player import *
from card import *


class CardHandler:
    def __init__(self, players, card_types):
        self.players = players
        self.card_types = card_types
        self.all_cards = self.create_cards()
        self.distribute_cards()

    def create_cards(self):
        all_cards = []
        for card_type in self.card_types:
            all_cards.extend([Card(f"Card {i+1}", card_type) for i in range(len(self.players))])
        return all_cards

    def distribute_cards(self):
        num_players = len(self.players)
        num_cards_per_player = len(self.all_cards) // num_players
        random.shuffle(self.all_cards)

        for i, player in enumerate(self.players):
            start_index = i * num_cards_per_player
            end_index = (i + 1) * num_cards_per_player

            player.card_stack.extend(self.all_cards[start_index:end_index])

    def inspect_cards(self):
        for player in self.players:
            print(f"{player.name}'s card stack:")
            for card in player.card_stack:
                print(f"{card.name} ({card.card_type})")