import sys
import pygame
from bullet import Bullet
from time import sleep

def checkKeydownEvents(event, aiSettings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.movingUp = True
    elif event.key == pygame.K_DOWN:
        ship.movingDown = True
        
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def checkKeyUpEvents(event, ship):
    if event.key == pygame.K_UP:
        ship.movingUp = False
    elif event.key == pygame.K_DOWN:
        ship.movingDown = False

def checkEvents(aiSettings, screen, ship, bullets, playButton, rectangle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, aiSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(aiSettings, playButton, mouseX, mouseY, ship, bullets, rectangle)

def checkPlayButton(aiSettings, playButton, mouseX, mouseY, ship, bullets, rectangle):
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClicked and not aiSettings.gameActive:
        aiSettings.resetStats()
        aiSettings.initializeDynamicSettings()
        pygame.mouse.set_visible(False)
        aiSettings.gameActive = True
        bullets.empty()
        ship.centerShip()
        rectangle.centerRectangle()

def updateRectangle(aiSettings, screen, rectangle):
    checkRectangleEdges(aiSettings, rectangle)
    rectangle.update()
    
def checkRectangleEdges(aiSettings, rectangle):
    if rectangle.checkEdges():
        aiSettings.rectangleDirection *= -1            

def updateScreen(aiSettings, screen, ship, bullets, rectangle, playButton):
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    rectangle.blitme()
    for bullet in bullets.sprites():
        bullet.drawBullet()
    if not aiSettings.gameActive:
        playButton.drawButton()

    pygame.display.flip()
    
def updateBullets(aiSettings, screen, ship, bullets, rectangle):
    bullets.update()
    screenRect = screen.get_rect()
    checkCollision(aiSettings, screen, ship, bullets, rectangle)
                
def fireBullet(aiSettings, screen, ship, bullets):
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)

def borderHit(aiSettings, screen, ship, bullets, rectangle):
    if aiSettings.lives > 0:
        aiSettings.lives -= 1
        sleep(0.5)
        bullets.empty()
        ship.centerShip()
        rectangle.centerRectangle()
    else: 
        aiSettings.gameActive = False
        pygame.mouse.set_visible(True)

def checkCollision(aiSettings, screen, ship, bullets, rectangle):
    screenRect = screen.get_rect()
    for bullet in bullets.sprites():
        if pygame.sprite.spritecollideany(rectangle, bullets):
            for bullet in bullets.sprites():
                aiSettings.increaseSpeed()
                bullets.remove(bullet)
        elif bullet.rect.right >= screenRect.right:
            borderHit(aiSettings, screen, ship, bullets, rectangle)
            break
