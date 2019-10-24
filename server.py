from flask import Flask, request
from flask_cors import CORS
import json
import xdrone

app = Flask(__name__)
CORS(app)

@app.route('/test')
def test():
    return "Hello world from flask backend!"

@app.route('/')
def root():
    return "Hello xDrone!"

@app.route('/fly', methods=['POST'])
def fly():
    data = request.get_json()
    program = data['body']['body']['program']
    xdrone.fly(program)
    return "Flight success"

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True,port=8081)
