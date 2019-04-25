#!/usr/bin/python3
'''TODO'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''TODO'''
    storage.reload()
    statesdict = storage.all("State")
    states = {}
    for _, v in statesdict.items():
        states[v.id] = v.name
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''TODO'''
    storage.reload()
    states = [[v.id, v.name] for v in storage.all("State").values()]
    c = storage.all("City")
    cities = {}
    for v in c.values():
        if v.state_id in cities.keys():
            cities[v.state_id].append([v.id, v.name])
        else:
            cities[v.state_id] = [[v.id, v.name]]
    return render_template('8-cities_by_states.html',
                           states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_storage(self):
    '''TODO'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
