"""
Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen, then match the background color of the image to the background color of the screen or vice versa.
"""
import pygame
import Character_class


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption("Blue sky")

        self.character = Character_class.Character(self)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Заполнение экрана цветом (например, белым)
            self.screen.fill((0, 184, 217))

            self.screen.blit(self.character.image, self.character.image_rect)

            # Обновление экрана
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
