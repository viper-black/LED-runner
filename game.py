import random
import keyboard

class Game:

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.size = gameDisplay.getSize()
        self.coinPos = random.randrange(1, self.size)
        self.enemyPos = random.randrange(5, self.size)
        while self.enemyPos == self.coinPos:
            self.coinPos = random.randrange(1, self.size)
        self.manPos = 0



    def tick(self):
        self.gameDisplay.display(self)

        if keyboard.is_pressed('d'):
            self.manPos = self.manPos + 1
        elif keyboard.is_pressed('a'):
            self.manPos = self.manPos - 1    
