#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request, it removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """ displays HTML page with all states """
    States = storage.all(State).values()
    sorted_states = sorted(States, key=lambda s: s.name)
    return render_template("9-states.html", States=sorted_states, one=None)


@app.route('/states/<string:id>', strict_slashes=False)
def display_state_cities(id):
    """ displays one state if it exists """
    key = "State." + id
    one = None
    if key in storage.all(State):
        one = storage.all(State)[key]
    return render_template("9-states.html", States=None, one=one)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
