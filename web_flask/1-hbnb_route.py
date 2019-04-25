#!/usr/bin/python3
'''
Starts a Flask web application listening on 0.0.0.0, port 5000

$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:
$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Defines body of response to GET request at `root` location'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Defines body response to GET request `hbnb` location'''
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
