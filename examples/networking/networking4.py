
# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()

import ntptime
import utime
import mip

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to TRENDHIM WIFI...')
        wlan.connect('AHA', 'SECRET')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    ntptime.settime()
    print(utime.localtime())
    import mip
    
do_connect()

# mip.install('ssd1306')
# eller mip.install('ssd1306', mpy=False)

