
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #initalize game and creates the screen object
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode((si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("SLU Invaders")
    play_button = Button(si_settings,screen,"Play Now")
    #set background color
    bg_color = (230,230,230)
    #Make a ship
    ship = Ship(si_settings, screen)
    #Group for bullets
    bullets = Group()
    #make aliens
    aliens = Group()
    gf.create_fleet(si_settings,screen,ship,aliens)
    stats = GameStats(si_settings)
    sb = Scoreboard(si_settings,screen,stats)
    #Start main loop for game
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(si_settings, screen,stats,sb,play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(si_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(si_settings,screen,stats,sb,ship, aliens,bullets)
        gf.update_screen(si_settings,screen,stats,sb,ship,aliens,bullets,play_button)







run_game()
