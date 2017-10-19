import sys
import pygame

def check_events(ship):
    """Respond to key presses and mouse input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
                #Move the ship to the LEFT
                ship.rect.centerx -= 1

def update_screen(si_settings,screen,ship):
    """Updates images on screen and writes new screen"""
    #Redraw the screen each time through loop
    screen.fill(si_settings.bg_color)
    ship.blitme()
    #Makes most recent drawn screen visible
    pygame.display.flip()
