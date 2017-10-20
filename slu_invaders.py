
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initalize game and creates the screen object
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode((si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("SLU Invaders")
    #set background color
    bg_color = (230,230,230)
    #Make a ship
    ship = Ship(si_settings, screen)
    #Group for bullets
    bullets = Group()
    #Start main loop for game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(si_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(si_settings,screen,ship,bullets)
        #Get rid of off scrren bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                print(len(bullets))






run_game()
