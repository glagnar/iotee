from machine import Pin
from time import sleep
import dht

import network
from ntptime import settime

from simple import MQTTClient

sensor = dht.DHT22(Pin(32))

def do_networking():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect("GIOT", "GIOTGIOTGIOT")
        while not wlan.isconnected():
            pass
    print("network config:", wlan.ifconfig())

    from ntptime import settime

    settime()

    import utime
    print(utime.localtime())

do_networking()

client = MQTTClient('12345656789', '172.20.10.3')
client.connect()

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: %3.1f C" % temp)
        print("Humidity: %3.1f %%" % hum)
        
        client.publish('temperatur', str(temp))

    except OSError as e:
        print("Failed to read sensor." + e)
