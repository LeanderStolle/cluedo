import pygame
import MainMenu
import Board

class CluedoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cluedo Game")
        self.Clue_board = Board.Board()
        self.menu = MainMenu.MainMenu(self)
        self.current_state = "menu"

    def switch_to_gameplay(self):
        self.current_state = "gameplay"
        self.Clue_board.draw_board(self.screen)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if self.current_state == "menu":
                    self.menu.run(self.screen)
                elif self.current_state == "gameplay":
                    self.Clue_board.draw_board(self.screen)

            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = CluedoGame()
    game.run()




