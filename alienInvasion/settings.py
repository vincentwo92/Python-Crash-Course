class Settings():
    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)
        
        self.shipSpeedFactor = 1
        self.shipLimit = 3

        self.bulletSpeedFactor = 3
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 3
        
        self.alienSpeedFactor = 0.35
        self.fleetDropSpeed = 15
        self.fleetDirection = 1

        self.speedupScale = 1.1
        self.scoreScale = 1.5
        
        self.initializeDynamicSettings()
        
    def initializeDynamicSettings(self):
        self.shipSpeedFactor = 1
        self.bulletSpeedFactor = 3
        self.alienSpeedFactor = 0.15
        
        self.fleetDirection = 1
        
        self.alienPoints = 50
        
    def increaseSpeed(self):
        self.shipSpeedFactor *= self.speedupScale
        self.bulletSpeedFactor *= self.speedupScale
        self.alienSpeedFactor *= self.speedupScale
        self.alienPoints = int(self.alienPoints * self.scoreScale)
        print(self.alienPoints)
