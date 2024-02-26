from machine import Pin
from neopixel import NeoPixel

pin = Pin(15, Pin.OUT)        # set GPIO15 to output to drive NeoPixels
np = NeoPixel(pin, 7, bpp=4)  # create NeoPixel driver on GPIO15 for 7 pixels, 4 colours

for i in range(np.n):
    np[i] = (255, 255, 255, 255)    # PRESS ENTER THREE TIMES IN IN REPL

np.write()


