import random

class Game:

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.size = gameDisplay.getSize()

        self.enemyPos = random.randrange(5, self.size)
        self.coinPos = random.randrange(1, self.size)
        self.manPos = 0


    def tick(self):
        self.gameDisplay.display(self)