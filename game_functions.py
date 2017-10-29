import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(si_settings, screen,stats,sb,play_button, ship,aliens, bullets):
    """Respond to key presses and mouse input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, si_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(si_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)


def check_play_button(si_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """Start a new game when you click play"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Hides mouse
        pygame.mouse.set_visible(False)
        #reset stats
        si_settings.initalize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        #reset Scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #Empty aliens and bullets
        aliens.empty()
        bullets.empty()
        #creates new fleet and centers ship
        create_fleet(si_settings,screen,ship,aliens)
        ship.center_ship()

def fire_bullet(si_settings, screen,ship,bullets):
    """Fires bullet if limit not reached"""
    if len(bullets) < si_settings.bullets_allowed:
        new_bullet = Bullet(si_settings, screen, ship)
        bullets.add(new_bullet)



def update_screen(si_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """Updates images on screen and writes new screen"""
    #Redraw the screen each time through loop
    screen.fill(si_settings.bg_color)
    #Redraws bullets behind ship and invaders
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #Draws score
    sb.show_score()
    #Draw button if game not active
    if not stats.game_active:
        play_button.draw_button()
    #Makes most recent drawn screen visible
    pygame.display.flip()

def update_bullets(si_settings,screen,stats,sb,ship,aliens,bullets):
    #updates bullets and gets rif=d of old ones
    bullets.update()
    #Get rid of off scrren bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(si_settings, screen,stats,sb, ship, aliens, bullets)


def check_bullet_alien_collisions(si_settings, screen,stats,sb, ship, aliens, bullets):
    #Check if bullets hit aliens and removes both
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += si_settings.alien_points * len(aliens)
            sb.prep_score()
            check_high_score(stats,sb)
    if len(aliens) == 0:
        #destroy bullets and make new fleet
        bullets.empty()
        si_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(si_settings,screen,ship,aliens)



def get_number_aliens_x(si_settings,alien_width):
    """determine number of aliens on row"""
    available_space_x = si_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(si_settings,screen,aliens,alien_number,row_number):
    #creates alien on row
    alien = Alien(si_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(si_settings,ship_height,alien_height):
    """Determines how many rows of aliens can fit """
    available_space_y = (si_settings.screen_height - (3*alien_height)- ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows



def create_fleet(si_settings,screen,ship,aliens):
    """Create a fleet of aliens"""
    #creates an alien and finds the number in a row
    #each alien has has space equal to one alien next to it
    alien = Alien(si_settings,screen)
    number_aliens_x = get_number_aliens_x(si_settings,alien.rect.width)
    number_rows = get_number_rows(si_settings,ship.rect.height,alien.rect.height)


    #Creates fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(si_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(si_settings, aliens):
    """respond if aliens reach the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(si_settings,aliens)
            break


def change_fleet_direction(si_settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += si_settings.fleet_drop_speed
    si_settings.fleet_direction *= -1


def update_aliens(si_settings,screen,stats,sb,ship,aliens,bullets):
    """ Check if aliesn at the edge and then updates position Updates aliens position"""
    check_fleet_edges(si_settings, aliens)
    aliens.update()
    #look for alien ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(si_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(si_settings,screen,stats,sb,ship,aliens,bullets)

def ship_hit(si_settings,screen,stats,sb,ship,aliens,bullets):
    """If ship is hit by aliens"""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        #update Scoreboard
        sb.prep_ships()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    #empties aliens and bullets
    aliens.empty()
    bullets.empty()
    #makes new aliens and centers ship
    create_fleet(si_settings,screen,ship,aliens)
    ship.center_ship()
    #stop
    sleep(0.5)


def check_aliens_bottom(si_settings,screen,stats,sb,ship,aliens,bullets):
    """Check for aliens touching screen bottom"""
    screen_rect= screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(si_settings,screen,stats,sb,ship,aliens,bullets)
            break

def check_high_score(stats,sb):
    """Check for new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
