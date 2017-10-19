import pygame

class Ship():
    def __init__(self,screen):
        """Initializes the ship and it's starting position"""
        self.screen = screen
        #Loads ship image and get it's rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Starts new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect)
