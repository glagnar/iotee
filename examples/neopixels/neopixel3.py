import machine
import neopixel, time

np = neopixel.NeoPixel(machine.Pin(14), 7, bpp=4)

def set_colourw(r, g, b, w):
    for i in range(7):
        np[i] = (r, g, b, w)
    np.write()

# Function for a smoother pulsating effect
def pulsew(r, g, b, w, delay):
    for intensity in range(10, 255, 5):  # Smaller step for smoother transition
        set_colourw(int(r*intensity/255), int(g*intensity/255), int(b*intensity/255), int(w*intensity/255))
        time.sleep_ms(delay)
    for intensity in range(255, 10, -5):  # Smaller step for smoother transition
        set_colourw(int(r*intensity/255), int(g*intensity/255), int(b*intensity/255), int(w*intensity/255))
        time.sleep_ms(delay)

while True:
    pulsew(50, 50, 100, 255, 20)  # Adjusted for smoother transition

