# YOU COULD MANUALLY TYPE 
# EACH LINE INTO YOUR REPL

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(14), 16, bpp=4, timing=1) # create NeoPixel driver on GPIO14 for 16 pixels, 4 colours
np[0] = (255, 0, 0, 0)                                       # set the first pixel to white - ZERO indexed
np.write()                                                   # write data to all pixels

