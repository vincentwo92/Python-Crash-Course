import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, aiSettings, screen, ship):
        super().__init__()
        self.screen = screen
        
        
        self.rect = pygame.Rect(0, 0, aiSettings.bulletHeight,
            aiSettings.bulletWidth)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        
        self.x = float(self.rect.x)
        
        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor
        
    def update(self):
        self.x += self.speedFactor
        self.rect.x = self.x
        
    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
