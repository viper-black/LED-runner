import time
import sys
from game import Game

display = None
if len(sys.argv) > 1 and sys.argv[1] == 'led':
    from ledGameDisplay import LedGameDisplay
    display = LedGameDisplay()
else:
    from consoleGameDisplay import ConsoleGameDisplay
    display = ConsoleGameDisplay()

my_game = Game(display)

while not my_game.isOver:
    time.sleep(0.05)
    my_game.tick()