import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, set, screen):
        super().__init__()
        self.set = set  # initialize alien and starting position
        self.screen = screen

        self.image = pygame.image.load('Images/alien.bmp')  # loading the alien image
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  # Placing the ship in the top left corner of the screen
        self.rect.y = self.rect.height  # leaving the  space equal to width of the image

        self.x = float(self.rect.x)  # Storing the postion of alien

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
       self.x += self.set.alien_speed_factor
       self.rect.x = self.x
