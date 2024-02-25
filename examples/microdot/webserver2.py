from microdot import Microdot, redirect
app = Microdot()

html = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Burning Lights</h1>
        <p>
            <a href="/on">Lights ON</a> <a href="/off">Lights OFF</a>
        </p>
    </body>
</html>
'''

@app.route('/')
async def index(request):
    global index
    return str(html), 200, {'Content-Type': 'text/html'}

@app.route('/on')
async def web_on(request):
    print('on')
    return redirect('/')

@app.route('/off')
async def web_off(request):
    print('off')
    return redirect('/')

app.run(debug=True, port=80)


