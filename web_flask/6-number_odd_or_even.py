#!/usr/bin/python3
""" This module will start the flask web application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Start flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """route to hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_route(text):
    """route text and remove underscores"""
    new_text = "C " + text.replace("_", " ")
    return new_text


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """route for python and return string"""
    new_text = "Python " + text.replace("_", " ")
    return new_text


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """check the type of a parameter"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_route_template(n):
    """render template of html"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oe_template(n):
    """render templates even or odd"""
    value = "even" if n % 2 == 0 else "odd"
    value = f"{n} is " + value
    return render_template('6-number_odd_or_even.html', evenorodd=value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
