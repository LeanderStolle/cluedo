import pygame
import MainMenu
import Board


#Klasse für das Spiel erzeugt im Konstruktor alle nötigen Instanzen der einzelnen Klassen/Objekte
class CluedoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Cluedo Game")
        self.Clue_board = Board.Board()
        self.menu = MainMenu.MainMenu(self)
        self.current_state = "menu"

    #ändern des Zustands
    def switch_to_gameplay(self):
        self.current_state = "gameplay"
        self.Clue_board.draw_board(self.screen)


    #Main Loop
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




