import random
import pygame
class Card:
    def __init__(self, name, card_type):
        self.name = name
        self.card_type = card_type
    def get_name(self):
        return self.name

    def draw_card(self,card, position,screen):
        x, y = position
        card_rect = pygame.Rect(x, y, 150, 150)  # Rectangle for the card

        # Set colors based on card type
        if card.card_type == "Room":
            card_color = (139, 69, 19)  # Brown for rooms
        elif card.card_type == "Character":
            card_color = (0, 0, 255)  # Blue for characters
        elif card.card_type == "Weapon":
            card_color = (255, 0, 0)  # Red for weapons

        pygame.draw.rect(screen, card_color, card_rect)  # Draw the card rectangle
        pygame.draw.rect(screen, (0, 0, 0), card_rect, 2)  # Draw the outline

        # Draw the card type and name text
        font = pygame.font.Font(None, 24)
        type_text = font.render("Type: " + card.card_type, True, (255, 255, 255))
        name_text = font.render("Name: " + card.name, True, (255, 255, 255))

        screen.blit(type_text, (x + 10, y + 10))
        screen.blit(name_text, (x + 10, y + 40))



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



