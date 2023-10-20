#!/usr/bin/python3
""" This module will start the flask web application
"""

from flask import Flask

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


@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """route for python and return string"""
    new_text = "Python " + text.replace("_", " ")
    return new_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
