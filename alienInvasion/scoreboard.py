import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self, aiSettings, screen, stats):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = stats
        
        self.textColor = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prepImages()
    
    def prepImages(self):
        self.prepScore()
        self.prepHighScore()
        self.prepLevel()
        self.prepShips()
        
    def prepScore(self):
        roundedScore = int(round(self.stats.score, -1))
        scoreStr = '{:,}'.format(roundedScore)
        self.scoreImage = self.font.render(scoreStr, True, self.textColor,
            self.aiSettings.bgColor)
            
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20
        
    def showScore(self):
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.levelImage, self.levelRect)
        self.ships.draw(self.screen)

    def prepHighScore(self):
        highScore = round(self.stats.highScore, -1)
        highScoreStr = '{:,}'.format(highScore)
        self.highScoreImage = self.font.render(highScoreStr, True,
            self.textColor, self.aiSettings.bgColor)
            
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top

    def prepLevel(self):
        self.levelImage = self.font.render(str(self.stats.level), True,
            self.textColor, self.aiSettings.bgColor)
            
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10

    def prepShips(self):
        self.ships = Group()
        for shipNumber in range(self.stats.shipsLeft):
            ship = Ship(self.aiSettings, self.screen)   
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
