# YOU COULD MANUALLY TYPE 
# EACH LINE INTO YOUR REPL

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(15), 7, bpp=4) # create NeoPixel driver on GPIO15 for 7 pixels, 4 colours
np[0] = (255, 255, 255, 255)	# set the first pixel to white - ZERO indexed
np.write()               		# write data to all pixels
r, g, b, w = np[0]       		# get first pixel colour
