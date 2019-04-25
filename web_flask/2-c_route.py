#!/usr/bin/python3
'''
Starts a Flask web application listening on 0.0.0.0, port 5000

Extra requirement:
/c/<text>: display “C ” followed by the value of the
text variable (replace underscore _ symbols with a space)

$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....

In another tab:
$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$

$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$

$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you \
entered the URL manually please check your spelling and try again.</p>
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Defines body of response to GET request to `root` location'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Defines body of response to GET request to `hbnb` location'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Defines body of response to GET request to `c/<text>` location'''
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
