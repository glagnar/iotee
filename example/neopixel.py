from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)   # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, 1)    # create NeoPixel driver on GPIO14 for 1 pixels
np[0] = (255, 255, 255)  # set the first pixel to white
np.write()               # write data to all pixels
r, g, b = np[0]          # get first pixel colour
