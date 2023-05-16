#!/usr/bin/python3
"""Write a script that starts a Flask web application
and would be listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' on the home page."""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB' on the /hbnb route."""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C ' followed by the value of the text variable
    (replace underscore _ symbols with a space) on the /c/<text> route."""
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Displays 'Python ' followed by the value of the text variable
    (replace underscore _ symbols with a space) on the /python/<text> route.
    The default value of text is 'is cool'."""
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """function2"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer.
    The HTML page displays a header tag with the text
    'Number: n' inside the body."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if n is an integer:
    H1 tag: 'Number: n is even|odd' inside the tag BODY"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
