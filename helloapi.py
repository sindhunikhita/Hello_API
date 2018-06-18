from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name="Stranger"):
    return "Hello %s!"%(name)

run(app, host='localhost', port=80)
