import pygame
import sys
from Player import Player

pygame.init()


board_image = pygame.image.load("src/clue_board.jpg")
board_width, board_height = board_image.get_size()


SCREEN_WIDTH, SCREEN_HEIGHT = board_width, board_height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60

pygame.display.set_caption("Clue Game")


def main():
    player1 = Player("Player 1", (100, 100))

    # Sprite Groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)


    clock = pygame.time.Clock()
    #main loop
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


        # Update game objects
        all_sprites.update()

        # Clear the screen
        #screen.fill((255, 255, 255))
        screen.blit(board_image, (0, 0))


        # Draw game objects
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()




