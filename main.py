import pygame
from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(set, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(set, screen, ship)
        pygame.display.flip()  # update the screen


run_game()
