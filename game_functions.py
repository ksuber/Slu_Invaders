import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, si_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move the ship to the LEFT
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Creates new bullet and adds to bullet Group
        fire_bullet(si_settings,screen,ship,bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(si_settings, screen, ship, bullets):
    """Respond to key presses and mouse input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, si_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(si_settings, screen,ship,bullets):
    """Fires bullet if limit not reached"""
    if len(bullets) < si_settings.bullets_allowed:
        new_bullet = Bullet(si_settings, screen, ship)
        bullets.add(new_bullet)



def update_screen(si_settings,screen,ship,bullets):
    """Updates images on screen and writes new screen"""
    #Redraw the screen each time through loop
    screen.fill(si_settings.bg_color)
    #Redraws bullets behind ship and invaders
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #Makes most recent drawn screen visible
    pygame.display.flip()

def update_bullet(bullets):
    #updates bullets and gets rif=d of old ones
    bullets.update()
    #Get rid of off scrren bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))
