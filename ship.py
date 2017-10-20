import pygame

class Ship():
    def __init__(self, si_settings, screen):
        """Initializes the ship and it's starting position"""
        self.screen = screen
        self.si_settings = si_settings
        #Loads ship image and get it's rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Starts new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ moves ship based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.si_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.si_settings.ship_speed_factor



    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect)
