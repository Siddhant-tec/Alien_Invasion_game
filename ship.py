import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen  # initialize the starting position

        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()  # rect is actually the ship
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx  # putting ship image on the bottom-center
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
