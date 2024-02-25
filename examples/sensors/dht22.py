from machine import Pin
from time import sleep
import dht

# For the FeatherV2 we need to put this pin high.
# p0 = Pin(2, Pin.OUT)
# p0.value(1)

sensor = dht.DHT22(Pin(20))

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: %3.1f C" % temp)
        print("Humidity: %3.1f %%" % hum)
    except OSError as e:
        print("Failed to read sensor." + e)

