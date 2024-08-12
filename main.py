
import flask

app=flask.Flask(__name__)

@app.route('/')
def f():
	return 'Hello World'


app.run(port=80,host='0.0.0.0')





