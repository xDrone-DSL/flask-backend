from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return "Hello world from flask backend!"

@app.route('/')
def root(): 
    return "Hello xDrone!"


if __name__ =="__main__":
    app.run(debug=True,port=65535)