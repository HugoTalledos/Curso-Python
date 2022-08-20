from flask import Flask

app = Flask(__name__)

@app.route('/')		#se le dice al servidor en que url se ejecuta la funcion 

def hello_world():
	return 'Hola, HUGO.'

if __name__ == '__main__':
	app.run()