import sys
import pygame
from bullets import Bullet
from alien import Alien


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


def update_screen(set, screen, ship, aliens, bullets):
    screen.fill(set.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)


def fire_bullets(set, screen, ship, bullets):
    new_bullet = Bullet(set, screen, ship)
    bullets.add(new_bullet)


def update_bullets(bullets):
    bullets.update()
    # Deleting bullets leaving the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(set, alien_width):
    available_space_x = set.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # Determine the number of aliens that fit in a row
    return number_aliens_x

def create_alien(set, screen, aliens, alien_number):
    alien = Alien(set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(set, screen, aliens):
    alien = Alien(set, screen)
    number_aliens_x = get_number_aliens_x(set, alien.rect.width)

    # creating rows of aliens
    for alien_number in range(number_aliens_x):
        create_alien(set, screen, aliens, alien_number)



