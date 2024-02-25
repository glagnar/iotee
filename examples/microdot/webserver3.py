from microdot import Microdot, redirect
app = Microdot()

from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)         # set GPIO14 to output to drive NeoPixels
np = NeoPixel(pin, 16, bpp=4)  # create NeoPixel driver on GPIO14 for 16 pixels, 4 colours

def lights_on():
    for i in range(np.n):
        np[i] = (255, 0, 0, 0)  # PRESS ENTER THREE TIMES IN IN REPL
    np.write()

def lights_off():
    for i in range(np.n):
        np[i] = (0, 0, 0, 0)    # PRESS ENTER THREE TIMES IN IN REPL
    np.write()
    
html = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Burning Lights</h1>
        <p>
            <a href="/on"><button>Lights ON</button></a>
            <a href="/off">Lights OFF</a>
        </p>
    </body>
</html>
'''

@app.route('/')
async def index(request):
    return str(html), 200, {'Content-Type': 'text/html'}

@app.route('/on')
async def web_on(request):
    lights_on()
    print('on')
    return redirect('/')

@app.route('/off')
async def web_off(request):
    lights_off()
    print('off')
    return redirect('/')

app.run(debug=True, port=80)




