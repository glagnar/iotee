import time
from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)         # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, 16, bpp=4)  # create NeoPixel driver on GPIO14 for 16 pixels, 4 colours


def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0, 0)
        np[i % n] = (255, 255, 255, 255)
        np.write()
        time.sleep_ms(50)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0,0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0, 0)
        np.write()
        time.sleep_ms(120)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0, 0)
    np.write()