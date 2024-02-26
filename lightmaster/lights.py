from machine import Pin
from neopixel import NeoPixel
import time
import uasyncio

pin = Pin(14, Pin.OUT)         # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, 16, bpp=4)  # create NeoPixel driver on GPIO14 for 16 pixels, 4 colours

def lights_on():
    for i in range(np.n):
        np[i] = (0, 0, 0, 255)
    np.write()

def lights_off():
    for i in range(np.n):
        np[i] = (0, 0, 0, 0)
    np.write()

def lights_rgbw(rgbw_tuple):
    for i in range(np.n):
        np[i] = rgbw_tuple
    np.write()

async def pulsew():
    while True:
        rgbw_tuple = (50, 50, 100, 255)
        for intensity in range(10, 255, 5):  # Smaller step for smoother transition
            lights_rgbw((int(rgbw_tuple[0]*intensity/255), int(rgbw_tuple[1]*intensity/255), int(rgbw_tuple[2]*intensity/255), int(rgbw_tuple[3]*intensity/255)))
            await uasyncio.sleep_ms(20)
        for intensity in range(255, 10, -5):  # Smaller step for smoother transition
            lights_rgbw((int(rgbw_tuple[0]*intensity/255), int(rgbw_tuple[1]*intensity/255), int(rgbw_tuple[2]*intensity/255), int(rgbw_tuple[3]*intensity/255)))
            await uasyncio.sleep_ms(20)
