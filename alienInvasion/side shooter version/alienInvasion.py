
import pygame
from settings import Settings
from ship import Ship
import gameFunctions as gf
from pygame.sprite import Group
from rectangle import Rectangle
from button import Button

def runGame():
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode(
        (aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption('Alien Invasion')

    # pygame.mouse.set_visible(True)
    playButton = Button(aiSettings, screen, 'Play')
    ship = Ship(aiSettings, screen)
    rectangle = Rectangle(aiSettings, screen)
    bullets = Group()
    
    while True:
        gf.checkEvents(aiSettings, screen, ship, bullets, playButton, rectangle)
        if aiSettings.gameActive:
            ship.update()
            gf.updateRectangle(aiSettings, screen, rectangle)
            gf.updateBullets(aiSettings, screen, ship, bullets, rectangle)
        gf.updateScreen(aiSettings, screen, ship, bullets, rectangle,
            playButton)

runGame()
