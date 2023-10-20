#!/usr/bin/python3
""" This module will start the flask web application
"""

from flask import Flask

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_route():
    """Start flask web application"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
