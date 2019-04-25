#!/usr/bin/python3
'''
Starts a Flask web application listening on 0.0.0.0, port 5000

$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:
$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)  # task requirement
def index():
    '''Defines body of response to GET request at `root` location'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
