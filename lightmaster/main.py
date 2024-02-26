from microdot import Microdot, redirect, send_file
from machine import Pin
import uasyncio
app = Microdot()

import lights

led = Pin(13, Pin.OUT)         # set GPIO14 to output to drive NeoPixels
async def blinkLed():
    while True:
        led.on()
        await uasyncio.sleep_ms(20)
        led.off()
        await uasyncio.sleep_ms(20)

current_task = None

@app.before_request
async def pre_request_handler(request):
    print("pre-request", current_task)
    if current_task:
        current_task.cancel()

@app.route('/')
async def index(request):
    return send_file('/static/index.html')

@app.route('/on')
async def web_on(request):
    lights.lights_on()
    print('on')
    return redirect('/')

@app.route('/off')
async def web_off(request):
    lights.lights_off()
    print('off')
    return redirect('/')

@app.route('/rgbw')
async def web_rgbw(request):
    lights.lights_rgbw((int(request.args['r']), int(request.args['g']), int(request.args['b']), int(request.args['w'])))
    print('rgbw')
    return redirect('/')

@app.route('/ironman')
async def web_ironman(request):
    global current_task
    current_task = uasyncio.create_task(lights.pulsew())
    return "ok"

@app.route('/static/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)

app.run(debug=True, port=80)



