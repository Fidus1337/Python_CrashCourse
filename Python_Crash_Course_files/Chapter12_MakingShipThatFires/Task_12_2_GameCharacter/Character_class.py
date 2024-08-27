import pygame


class Character:
    def __init__(self, game_window) -> None:
        self.image = pygame.image.load(
            "Python_Crash_Course_files/Chapter12_MakingAliensGame/Task_12_2_GameCharacter/ship.bmp")
        self.image_rect = self.image.get_rect()
        self.image_rect.center = game_window.screen_rect.center
