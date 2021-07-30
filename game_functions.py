import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(set, screen, ship):
    screen.fill(set.bg_color)
    ship.blitme()
