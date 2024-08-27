import pygame


class Rocket:
    def __init__(self, game_window) -> None:
        self.image = pygame.image.load(
            "Python_Crash_Course_files\Chapter12_MakingShipThatFires\Task_12_4_Rocket\cohete_off.png")
        self.image_rect = self.image.get_rect()
        # Изменение размера изображения
        # Укажите нужный размер (ширина, высота)
        self.image = pygame.transform.scale(self.image, (50, 100))

        self.image_rect.center = game_window.screen.get_rect().center
