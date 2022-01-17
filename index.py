import time
from game import Game
from consoleGameDisplay import ConsoleGameDisplay
dispay = ConsoleGameDisplay()
#from ledGameDisplay import LedGameDisplay
#dispay = LedGameDisplay()

dispay = ConsoleGameDisplay()
my_game = Game(dispay)

while True:
    time.sleep(0.1)
    my_game.tick()