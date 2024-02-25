from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)        # set GPIO15 to output to drive NeoPixels
np = NeoPixel(pin, 16, bpp=4)  # create NeoPixel driver on GPIO14 for 7 pixels, 4 colours

def lights_on():
    for i in range(np.n):
        np[i] = (0, 0, 0, 255)    # PRESS ENTER THREE TIMES IN IN REPL
    np.write()

def lights_off():
    for i in range(np.n):
        np[i] = (0, 0, 0, 0)    # PRESS ENTER THREE TIMES IN IN REPL
    np.write()
    

