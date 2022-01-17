from gameDisplay import GameDisplay
from rpi_ws281x import *

LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

class LedGameDisplay(GameDisplay):

    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()

    def display(self, game):
        for idx in range(self.getSize()):
            self.strip.setPixelColor(idx, Color(0,0,0))
        self.strip.setPixelColor(game.manPos, Color(0,0,255))
        self.strip.setPixelColor(game.enemyPos, Color(255,0,0))
        self.strip.setPixelColor(game.coinPos, Color(247,215,9))
        self.strip.show()
        
    def displayGameOver(self):
        for idx in range(self.getSize()):
            self.strip.setPixelColor(idx, Color(255,0,0))
        self.strip.show()

    def getSize(self):
        return LED_COUNT
