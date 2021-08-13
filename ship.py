import pygame


class Ship():
    def __init__(self, set, screen):
        self.screen = screen  # initialize the starting position
        self.set = set

        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()  # rect is actually the ship
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx  # putting ship image on the bottom-center
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False  # Movement flag
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
            self.center += self.set.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
            self.center += self.set.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
