"""
Make a Pygame window with a blue background
"""
import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Blue sky")

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Filling the screen with color
            self.screen.fill((0, 184, 217))

            # Updating the screen
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
