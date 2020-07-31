import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('IDA', 'IDAIDAIDA')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

from ntptime import settime
settime()

import utime
print(utime.localtime())

