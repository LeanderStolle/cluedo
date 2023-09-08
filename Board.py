import pygame


    #def __init__(self):
       #self.board_image = pygame.image.load("clue_board.jpg")

class Board:
    def __init__(self):
        self.cluedo_board = [
            [2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 2],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 2]
        ]

    def draw_board(self, screen):
        cell_size = 50  # Größe jeder Zelle
        for row in range(len(self.cluedo_board)):
            for col in range(len(self.cluedo_board[0])):
                cell =self.cluedo_board[row][col]
                color = (255, 255, 255) if cell == 0 else (0, 0, 0)  # Frei: Weiß, Raum/Wand: Schwarz

                pygame.draw.rect(screen, color, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))