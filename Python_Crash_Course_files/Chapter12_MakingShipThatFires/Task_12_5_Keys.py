"""
: Make a Pygame file that creates an empty screen. In the event loop,
print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run
the program and press various keys to see how Pygame responds.
"""
import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Keys")

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        print("Pressed 0")
                    elif event.key == pygame.K_1:
                        print("Pressed 1")
                    elif event.key == pygame.K_2:
                        print("Pressed 2")
                    elif event.key == pygame.K_3:
                        print("Pressed 3")

            # Updating the screen
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
