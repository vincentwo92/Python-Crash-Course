class Settings():
    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)
        
        self.rectangleDirection = -1

        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 1

        self.gameActive = False
        self.lives = 3
        
        self.speedupScale = 1.1

        self.initializeDynamicSettings()
        
    def resetStats(self):
        self.lives = 3
    
    def initializeDynamicSettings(self):
        self.shipSpeedFactor = 1
        self.bulletSpeedFactor = 1
        self.rectangleSpeedFactor = 0.35
        
        self.rectangleDirection = -1
        
    def increaseSpeed(self):    
        self.shipSpeedFactor *= self.speedupScale 
        self.bulletSpeedFactor *= self.speedupScale 
        self.rectangleSpeedFactor *= self.speedupScale 
