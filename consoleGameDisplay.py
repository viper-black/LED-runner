from gameDisplay import GameDisplay
import sys

class ConsoleGameDisplay(GameDisplay):

    def __init__(self):
        pass

    def display(self, game):
        sys.stdout.write('\r')
        for idx in range(self.getSize()):
            if game.manPos == idx:
                sys.stdout.write('I')
            elif game.enemyPos == idx:
                sys.stdout.write('E')
            elif game.coinPos == idx:
                sys.stdout.write('o')
            else:
                sys.stdout.write('-')
                
    def displayGameOver(self):
        print('Game over!')

    def getSize(self):
        return 6