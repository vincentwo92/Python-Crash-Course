import pygame

class Rectangle():
    def __init__(self, aiSettings, screen):
        self.screen = screen
        self.aiSettings = aiSettings
        
        self.width, self.height = 50, 200
        self.rectangleColor = (0, 255, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        self.screenRect = screen.get_rect()
        
        self.rect.centery = self.screenRect.centery
        self.rect.right = self.screenRect.right
        
        self.center = float(self.rect.centery)
        
    def checkEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.bottom >= screenRect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
        
    def update(self):
        self.center += (self.aiSettings.rectangleSpeedFactor *
            self.aiSettings.rectangleDirection)
        self.rect.centery = self.center
        
    def blitme(self):
        self.screen.fill(self.rectangleColor, self.rect)

    def centerRectangle(self):
        self.center = self.screenRect.centery
