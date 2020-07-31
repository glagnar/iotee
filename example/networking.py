import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('GIOT', 'GIOTGIOTGIOT')
print('IP address:', wlan.ifconfig()[0])

# Sæt klokken
from ntptime import settime
settime()

# Se hvad klokken er
import utime
utime.localtime()
