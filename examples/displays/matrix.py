# MicroPython
from ht16k33matrixfeatherwing import HT16K33MatrixFeatherWing
from machine import SoftI2C, Pin

# Update the pin values for your board
DEVICE_I2C_SCL_PIN = 20
DEVICE_I2C_SDA_PIN = 22

i2c = SoftI2C(scl=Pin(DEVICE_I2C_SCL_PIN), sda=Pin(DEVICE_I2C_SDA_PIN))
led = HT16K33MatrixFeatherWing(i2c)

text = ".... Trendhim Rocks!!! ....... T-R-END T-R-END ...."
while True:
    led.scroll_text(text)
