from machine import Pin, I2C, SoftI2C
import ssd1306
import utime

# using default address 0x3C
i2c = SoftI2C(sda=Pin(5), scl=Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Trendhim Rocks!', 0, 0, 1)
display.show()
