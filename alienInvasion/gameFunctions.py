import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import json

def checkKeydownEvents(event, aiSettings, screen, stats, sb, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
        
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        filename = 'highscore.json'
        with open(filename, 'w') as fileObject:
            json.dump(stats.highScore, fileObject)
        sys.exit()
        
    elif event.key == pygame.K_p and not stats.gameActive:
        startGame(aiSettings, screen, stats, sb, ship, aliens, bullets)
        
def checkKeyUpEvents(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False

def checkEvents(aiSettings, screen, stats, sb, playButton, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            filename = 'highscore.json'
            with open(filename, 'w') as fileObject:
                json.dump(stats.highScore, fileObject)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(aiSettings, screen, stats, sb, playButton, ship, aliens,
                bullets, mouseX, mouseY)
            
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, aiSettings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)

def checkPlayButton(aiSettings, screen, stats, sb, playButton, ship, aliens,
    bullets, mouseX, mouseY):
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClicked and not stats.gameActive:
        aiSettings.initializeDynamicSettings()
        startGame(aiSettings, screen, stats, sb, ship, aliens, bullets)
        
def startGame(aiSettings, screen, stats, sb, ship, aliens, bullets):
    pygame.mouse.set_visible(False)
    stats.resetStats()
    stats.gameActive = True
    
    sb.prepImages()
        
    aliens.empty()
    bullets.empty()
    
    createFleet(aiSettings, screen, ship, aliens)
    ship.centerShip()
        
def updateScreen(aiSettings, screen, stats, sb, ship, aliens, bullets, playButton):
    screen.fill(aiSettings.bgColor)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    sb.showScore()
    if not stats.gameActive:
        playButton.drawButton()

    pygame.display.flip()
    
def updateBullets(aiSettings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    checkBulletAlienCollisions(aiSettings, screen, stats, sb, ship, aliens, bullets)
    
def checkBulletAlienCollisions(aiSettings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += aiSettings.alienPoints * len(aliens)
            sb.prepScore()
        checkHighScore(stats, sb)
    if len(aliens) == 0:
        startNewLevel(aiSettings, screen, stats, sb, ship, aliens, bullets)
        
def startNewLevel(aiSettings, screen, stats, sb, ship, aliens, bullets):
    bullets.empty()
    aiSettings.increaseSpeed()
    stats.level += 1
    sb.prepLevel()
    createFleet(aiSettings, screen, ship, aliens)
    
def fireBullet(aiSettings, screen, ship, bullets):
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)
        
def createFleet(aiSettings, screen, ship, aliens):
    alien = Alien(aiSettings, screen)
    numberAliensX = getNumberAliensX(aiSettings, alien.rect.width)
    numberRows = getNumberRows(aiSettings, ship.rect.height, alien.rect.height)
    
    for rowNumber in range(numberRows):
        for alienNumber in range(numberAliensX):
            createAlien(aiSettings, screen, aliens, alienNumber, rowNumber)

def getNumberAliensX(aiSettings, alienWidth):
    availableSpaceX = aiSettings.screenWidth - 2 * alienWidth
    numberAliensX = int(availableSpaceX / (2 * alienWidth))
    return numberAliensX
    
def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width 
    alien.x = alienWidth + 2 * alienWidth * alienNumber 
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber 
    aliens.add(alien)
    
def getNumberRows(aiSettings, shipHeight, alienHeight):
        availableSpaceY = (aiSettings.screenHeight - 
            (3 * alienHeight) - shipHeight)
        numberRows = int(availableSpaceY / (2 * alienHeight))
        return numberRows
        
def updateAliens(aiSettings, stats, screen, sb, ship, aliens, bullets):
    checkFleetEdges(aiSettings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(aiSettings, stats, screen, sb, ship, aliens, bullets)
    checkAliensBottom(aiSettings, stats, screen, sb, ship, aliens, bullets)
    
def checkFleetEdges(aiSettings, aliens):
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, aliens)
            break
            
def changeFleetDirection(aiSettings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += aiSettings.fleetDropSpeed
    aiSettings.fleetDirection *= -1
    
def shipHit(aiSettings, stats, screen, sb, ship, aliens, bullets):
    if stats.shipsLeft > 0:
        stats.shipsLeft -= 1
        sb.prepShips()
        aliens.empty()
        bullets.empty()
        createFleet(aiSettings, screen, ship, aliens)
        ship.centerShip()
        sleep(0.5)
    else:
        stats.gameActive = False
        pygame.mouse.set_visible(True)
    
def checkAliensBottom(aiSettings, stats, screen, sb, ship, aliens, bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            shipHit(aiSettings, stats, screen, sb, ship, aliens, bullets)
            break
            
def checkHighScore(stats, sb):
    if stats.score > stats.highScore:
        stats.highScore = stats.score
        sb.prepHighScore()
