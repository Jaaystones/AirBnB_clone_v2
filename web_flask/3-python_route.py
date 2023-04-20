#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' on the home page."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' on the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C ' followed by the value of the text variable
    (replace underscore _ symbols with a space) on the /c/<text> route."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text=None):
    """Displays 'Python ' followed by the value of the text variable
    (replace underscore _ symbols with a space) on the /python/<text> route.
    The default value of text is 'is cool'."""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
