import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen  # initialize the starting position

        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()  # rect is actually the ship
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx  # putting ship image on the bottom-center
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False  # Movement flag
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
