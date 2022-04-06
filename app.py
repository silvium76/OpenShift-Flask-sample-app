from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! 4"

@app.route('/toys')
def toys():
    return "Hello World from toys"

@app.route('/cities')
def cities():
    return "Hello World from anywhere in the world"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
    # app.run(host='0.0.0.0', port=8080)
