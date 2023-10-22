#!/usr/bin/python3
""" This module will start the flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_apps(error):
    """This will tear down any data"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def filter_me():
    """find filters for me"""

    from models.state import State
    from models.amenity import Amenity

    listState = storage.all(State).values()
    listAmenity = storage.all(Amenity).values()
    return render_template("100-hbnb.html", listState=listState, listAmenity=listAmenity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
