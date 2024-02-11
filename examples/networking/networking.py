import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('AHA', 'SUPERSECRET')
print('IP address:', wlan.ifconfig()[0])

# set the internal clock
from ntptime import settime
settime()

# check what time it is
import utime
utime.localtime()
