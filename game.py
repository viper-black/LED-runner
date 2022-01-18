import random
import keyboard

class Game:

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.size = gameDisplay.getSize()
        self.initializeGame()
        
    def initializeGame(self):
        self.enemyPos = random.randrange(5, self.size)
        self.manPos = 0
        self.coinSpawn()
        self.isOver = False
        self.points = 0
        
    def coinSpawn(self):
        self.coinPos = random.randrange(1, self.size)
        while self.enemyPos == self.coinPos:
            self.coinPos = random.randrange(1, self.size)
        


    def tick(self):
        if self.isOver and keyboard.is_pressed(' '):
            self.initializeGame()
        
        if keyboard.is_pressed('d'):
            self.manPos = self.manPos + 1
        elif keyboard.is_pressed('a'):
            self.manPos = self.manPos - 1
        if self.manPos == -1:
            self.manPos = self.size - 1
        if self.manPos == self.size:
            self.manPos = 0
        if self.enemyPos > self.manPos:
            self.enemyPos = self.enemyPos -1
        if self.enemyPos < self.manPos:
            self.enemyPos = self.enemyPos + 1
        if self.manPos == self.enemyPos:
            self.gameDisplay.displayGameOver()
            self.isOver = True
            return
        if self.manPos == self.coinPos:
            self.coinSpawn()
            self.points = self.points + 1
            print(self.points)
        self.gameDisplay.display(self)
        
    
        

            