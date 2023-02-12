import pygame

class Ship():
    def __init__(self, aiSettings, screen):
        self.screen = screen
        self.aiSettings = aiSettings
        
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()
        
        self.rect.centery = self.screenRect.centery
        self.rect.left = self.screenRect.left
        
        self.center = float(self.rect.centery)
        
        self.movingUp = False
        self.movingDown = False
        
    def update(self):
        if self.movingDown and self.rect.bottom < self.screenRect.bottom:
            self.center += self.aiSettings.shipSpeedFactor
        if self.movingUp and self.rect.top > 0:
            self.center -= self.aiSettings.shipSpeedFactor
    
        self.rect.centery = self.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def centerShip(self):
        self.center = self.screenRect.centery
