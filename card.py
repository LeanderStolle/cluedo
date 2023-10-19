import random

class Card:
    def __init__(self, name, card_type):
        self.name = name
        self.card_type = card_type
    def get_name(self):
        return self.name



Kitchen_Card = Card("Kitchen", "Room")
Ballroom_Card = Card("Ballroom", "Room")
Conservatory_Card = Card("Conservatory", "Room")
Dining_Room_Card = Card("Dining Room","Room")
Billiard_Room_Card = Card("Billiard Room", "Room")
Library_Card = Card("Library", "Room")
Lounge_Card = Card("Lounge", "Room")
Hall_Card = Card("Hall", "Room")
Study_Card = Card("Study", "Room")
Rope_Card = Card("Rope", "Weapon")
Wrench_Card = Card("Wrench", "Weapon")
Revolver_Card = Card("Revolver", "Weapon")
Knife_Card = Card("Knife", "Weapon")
Candlestick_Card = Card("Candlestick", "Weapon")
Lead_Pipe_Card = Card("Lead Pipe", "Weapon")
Miss_Scarlett_Card = Card("Miss Scarlett", "Character")
Colonel_Mustard_Card = Card("Colonel Mustard", "Character")
Mrs_White_Card = Card("Mrs. White", "Character")
Mr_Green_Card = Card("Mr. Green", "Character")
Mrs_Peacock_Card = Card("Mrs. Peacock", "Character")
Professor_Plum_Card = Card("Professor Plum", "Character")



