from microdot import Microdot
app = Microdot()

@app.route('/')
async def index(request):
    return 'Hello, world!'

app.run(debug=True, port=80)
