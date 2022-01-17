import time
import sys
from game import Game

display = None
if sys.argv[1] == 'led':
    from ledGameDisplay import LedGameDisplay
    display = LedGameDisplay()
else:
    from consoleGameDisplay import ConsoleGameDisplay
    display = ConsoleGameDisplay()

my_game = Game(display)

while True:
    time.sleep(0.1)
    my_game.tick()