import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, aiSettings, screen):
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()
        
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        
        self.center = float(self.rect.centerx)
        
        self.movingRight = False
        self.movingLeft = False
        
    def update(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.aiSettings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.aiSettings.shipSpeedFactor
            
        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def centerShip(self):
        self.center = self.screenRect.centerx
