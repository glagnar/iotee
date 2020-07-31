from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)   # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, 7)    # create NeoPixel driver on GPIO14 for 7 pixels

for i in range(np.n):
    np[i] = (255, 255, 255) # TRYK ENTER TRE GANGE

np.write()

