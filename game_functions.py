import sys
import pygame
from bullets import Bullet


def check_keydown_events(event, set, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(set, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(set, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, set, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(set, screen, ship, bullets):
    screen.fill(set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()


def fire_bullets(set, screen, ship, bullets):
    new_bullet = Bullet(set, screen, ship)
    bullets.add(new_bullet)


def update_bullets(bullets):
    bullets.update()
    # Deleting bullets leaving the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
