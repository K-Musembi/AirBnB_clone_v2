#!/usr/bin/python3
"""A Flask web app"""


from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''Displays Hello HBNB'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays HBNB'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    '''Displays C followed by text'''
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    '''Dispalys Python followed by text'''

    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
