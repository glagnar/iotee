from machine import TouchPad, Pin
from neopixel import NeoPixel
import time
import _thread

# For the FeatherV2 we need to put this pin high.
p0 = Pin(2, Pin.OUT)
p0.value(1)

np = NeoPixel(Pin(0), 1, bpp=4)

# Define the interrupt service routine (ISR)
def touch_callback_on():
    np[0] = (255, 255, 255, 255)
    np.write()        

def touch_callback_off():
    np[0] = (0, 0, 0, 0)
    np.write()        

touch_pin = TouchPad(Pin(4))

def monitor_touch():
    touched = False
    while True:
        time.sleep_ms(500)
        if touch_pin.read() < 400:
            if not touched:
                touched = True
                touch_callback_on()
        else:
            if touched:
                touched = False
                touch_callback_off()  
                
_thread.start_new_thread(monitor_touch, ())
