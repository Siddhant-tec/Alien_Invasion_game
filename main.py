import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(set, screen)
    bullets = Group()
    aliens = Group()
    alien = Alien(set, screen)

    # Creating a fleet of aliens
    gf.create_fleet(set, screen, ship, aliens)

    while True:
        gf.check_events(set, screen, ship, bullets)
        ship.update()
        gf.update_bullets(set, screen, ship, aliens, bullets)
        gf.update_aliens(set, aliens)
        gf.update_screen(set, screen, ship, aliens, bullets)
        pygame.display.flip()  # update the screen


run_game()
