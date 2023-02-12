import pygame
from settings import Settings
from ship import Ship
import gameFunctions as gf
from pygame.sprite import Group
from gameStats import GameStats
from button import Button
from scoreboard import Scoreboard

def runGame():
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption('Alien Invasion')

    playButton = Button(aiSettings, screen, 'Play')
    stats = GameStats(aiSettings)
    sb = Scoreboard(aiSettings, screen, stats)
    ship = Ship(aiSettings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.createFleet(aiSettings, screen, ship, aliens)
    
    while True:
        gf.checkEvents(aiSettings, screen, stats, sb,  playButton, ship, aliens, bullets)
        if stats.gameActive:
            ship.update()
            gf.updateBullets(aiSettings, screen, stats, sb, ship, aliens, bullets)
            gf.updateAliens(aiSettings, stats, screen, sb, ship, aliens, bullets)
        gf.updateScreen(aiSettings, screen, stats, sb, ship, aliens, bullets, 
            playButton)

runGame()
