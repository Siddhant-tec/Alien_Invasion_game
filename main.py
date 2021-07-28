import pygame
import sys
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(set.bg_color)
        ship.blitme()
        pygame.display.flip()  # update the screen


run_game()
