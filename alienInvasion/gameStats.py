import json

class GameStats():
    def __init__(self, aiSettings):
        self.aiSettings = aiSettings
        self.resetStats()
        self.gameActive = False
        self.highScore = self.savedHighScore()
        
    def resetStats(self):
        self.shipsLeft = self.aiSettings.shipLimit
        self.score = 0
        self.level = 1
        
    def savedHighScore(self):
        filename = 'highScore.json'
        try: 
            with open(filename) as fileObject:
                return json.load(fileObject)
        except FileNotFoundError:
            return 0
