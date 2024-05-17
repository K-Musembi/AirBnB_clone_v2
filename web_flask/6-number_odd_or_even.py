#!/usr/bin/python3
"""A Flask web app"""


from flask import Flask, request, abort, render_template
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
def c(text):
    '''Displays C followed by text'''
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    '''Dispalys Python followed by text'''
    if text == '':
        text = "is cool"

    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    '''Check if it's a number'''
    try:
        num = int(n)
    except Exception as e:
        abort(404)

    if num:
        return f"{escape(num)} is a number"


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    '''Render html page if n is int'''
    try:
        num = int(n)
    except Exception as e:
        abort(404)

    if num:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    '''Render html page, n is odd or even'''
    try:
        num = int(n)
    except Exception as e:
        abort(404)

    value = "even" if num % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, value=value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
