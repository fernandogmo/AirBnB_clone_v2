#!/usr/bin/python3
'''
Before using Flask to display our HBNB data,
you will need to update some part of our engine:
'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''TODO'''
    storage.reload()
    statesdict = storage.all("State")
    states = []
    for v in statesdict.values():
        states.append([v.id, v.name])
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    '''TODO'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
