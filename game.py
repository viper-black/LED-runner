import time
import random
from rpi_ws281x import *
# LED strip configuration:

LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
enemy_pos = random.randrange(5, 150)
coin_pos = random.randrange(1, 150)


strip.setPixelColor(0, Color(0,0,255))
strip.setPixelColor(enemy_pos, Color(255,0,0))
strip.setPixelColor(coin_pos, Color(247,215,9))
strip.show()
