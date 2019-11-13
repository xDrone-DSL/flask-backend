from flask import Flask, request, jsonify
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
    address = data['body']['body']['address']
    xdrone.fly(program, address)
    return "Flight success"


@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    program = data['body']['body']['program']
    commands = xdrone.gen_simulate_commands(program)
    return jsonify({'commands': commands})


@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    program = data['body']['body']['program']
    bounds = data['body']['body']['bounds']
    result = xdrone.validate(program, bounds)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8081)
