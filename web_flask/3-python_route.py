#!/usr/bin/python3
""" Start a Flask application """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ displays hello hbnb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ displays C followed by <text>  content """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text=""):
    """ displays python followed by <text> content or default is cool"""
    if text:
        return f"Python {text.replace('_', ' ')}"
    else:
        return f"Python is cool"


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
