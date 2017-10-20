import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Used to manage bullets fired from ship"""
    def __init__(self,si_settings,screen,ship):
        """Creates bullet where ship is"""
        super().__init__()
        self.screen = screen
        #Create bullet rect at(0,0) and then places in correct position
        self.rect = pygame.Rect(0,0, si_settings.bullet_width, si_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Store bullet position as decimal
        self.y = float(self.rect.y)
        self.color = si_settings.bullet_color
        self.speed_factor = si_settings.bullet_speed_factor

    def update(self):
        """Moves bullet up screen"""
        #Update decimal position
        self.y -= self.speed_factor
        #Change rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
