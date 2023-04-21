#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""
from flask import Flask, request, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """/states_list folder
    storage.all() -> dictionary with objects of everything

    storage.all(State) -> dictionary with all instances of State

    storage.all(State).values() -> infomation of every State

    Returns:
        [HTML content: [display a HTML page: (inside the tag BODY)]
    """
    states = list(storage.all(State).values())
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def remove_session(exception):
    """after each request you must remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
