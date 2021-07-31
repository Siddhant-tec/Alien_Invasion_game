import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()
    set = Settings()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(set, screen)
    bullets = Group()

    while True:
        gf.check_events(set, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Deleting bullets leaving the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(set, screen, ship, bullets)
        pygame.display.flip()  # update the screen


run_game()
