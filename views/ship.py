import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('assets/icons/ship.bmp')
        self.image_rect = self.image.get_rect()

        # start each new ship at the bottom of screen
        self.image_rect.midbottom = self.screen_rect.midbottom

    def blit(self):
        # pygame will treat all elements like rects
        self.screen.blit(self.image, self.image_rect)
