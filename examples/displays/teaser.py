from machine import Pin, I2C, SoftI2C
import ssd1306
import utime

# using default address 0x3C
i2c = SoftI2C(sda=Pin(5), scl=Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Trendhim Rocks!', 0, 0, 1)
display.show()

WIDTH, HEIGHT = 128, 64  # Adjust these values based on your display
SCROLL_DELAY_MS = 150

def scroll_text(display, text_lines):
    text_height = len(text_lines) * 8  # Height of all lines
    y = 0  # Initial position for the first line

    while y > -text_height:
        display.fill(0)  # Clear the display
        for i, line in enumerate(text_lines):
            display.text(line, 0, y + i * 8)
        display.show()
        y -= 1
        utime.sleep_ms(SCROLL_DELAY_MS)

# Example multiline text
multiline_text = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "27th of February",
    "",
    "",
    "",
    "",
    "Everything      ",
    "        changed!",
    "",
    "",
    "  WILL THERE BE ",
    "    BEEEEER ??  ",
    "",
    "",
    "",
    "Have I been",
    "         hacked?",
    "",
    "",
    "",
    "",
    "Am    I   alive?",
    "",
    "",
    "",
    "",
    "",
    "WHO   IS   IKEA?",
    "",
    "",
    "",
    "AND WHAT IS THIS",
    "   LAMP BUSINESS",
    "   ALL ABOUT ?!?",
    "",
    "",
    "",
    "",
    "IS ENGINEERING  ",
    "OUT TO GET ME?!?",
    "",
    "",
    "",
    "",
    "",
    "Where am I ?",
    "",
    "",
    "",
    "",
    " ... _ _ _ ... ",
    " ... _ _ _ ... ",
    " ... _ _ _ ... ",
    " ... _ _ _ ... ",
    "",
    "",
    "",
    "... help m m me"
]

# Example usage
while True:
    scroll_text(display, multiline_text)
