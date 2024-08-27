import pygame
import sys
# pylint: disable=no-member

from rocket_class import Rocket


class Rocket_game:
    def __init__(self) -> None:
        pygame.init()

        self.time = pygame.time.Clock()
        self.bg_color = (78, 250, 12)

        self.screen = pygame.display.set_mode((1200, 800), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.rocket = Rocket(self)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        self.rocket.image_rect.x += 1
                    elif event.key == pygame.K_LEFT:
                        self.rocket.image_rect.x -= 1
                    elif event.key == pygame.K_UP:
                        self.rocket.image_rect.y -= 1
                    elif event.key == pygame.K_DOWN:
                        self.rocket.image_rect.y += 1

            # Ограничение FPS до 60 кадров в секунду
            self.time.tick(60)

            # Заливка экрана фоновым цветом
            self.screen.fill(self.bg_color)

            # Отрисовка ракеты
            self.screen.blit(self.rocket.image, self.rocket.image_rect)

            # Обновление экрана
            pygame.display.flip()


if __name__ == "__main__":
    game = Rocket_game()
    game.run_game()
