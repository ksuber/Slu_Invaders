import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class for alien ships"""
    def __init__(self,si_settings,screen):
        """ starts alien and sets position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.si_settings = si_settings
        #Load alien and sets rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #start alien in upper left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Stores aliens position
        self.x = float(self.rect.x)

    def check_edges(self):
        """ returns true if at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """Move alien right"""
        self.x += (self.si_settings.alien_speed_factor * self.si_settings.fleet_direction)
        self.rect.x = self.x


    def blitme(self):
        """Draw the Alien at the current location"""
        self.screen.blit(self.image, self.rect)
