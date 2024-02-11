from machine import Pin
from time import sleep
import dht

import ubinascii
import machine

from machine import Pin
from neopixel import NeoPixel

import network
from ntptime import settime

from example.mqtt.simple import MQTTClient

sensor = dht.DHT22(Pin(32))

pin = Pin(14, Pin.OUT)   # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, 1)    # create NeoPixel driver on GPIO14 for 1 pixels

def do_red():
    np[0] = (0, 255, 0)  # set the first pixel to red
    np.write()           # write data to all pixels

def do_blue():
    np[0] = (0, 0, 255)  # set the first pixel to blue
    np.write()           # write data to all pixels

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


def subscribe_callback(topic, msg):
    print((topic, msg))
    if topic == b"light" and msg == b"red":
        print("HOT STUFF - GOING RED")
        do_red()
    elif topic == b"light" and msg == b"blue":
        print("IT's COLD - GOING BLUE")
        do_blue()

def do_mqtt():
    client_id = ubinascii.hexlify(machine.unique_id())
    client = MQTTClient(client_id, "172.20.10.3")
    client.set_callback(subscribe_callback)
    client.connect()
    client.subscribe("light")
    return client

do_networking()

client = do_mqtt()

while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: %3.1f C" % temp)
        print("Humidity: %3.1f %%" % hum)
        client.check_msg()
        client.publish("temperatur", str(temp))

    except OSError as e:
        print("Bad stuff - restarting: " + str(e))
        sleep(10)
        machine.reset()
