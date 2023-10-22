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


@app.route("/states_list", strict_slashes=False)
def list_all_state():
    """render templates and jinja implementation"""
    from models.state import State

    stateList = storage.all(State).values()
    sorted_state_list = sorted(stateList, key=lambda state: state.name)
    return render_template('7-states_list.html', stateList=sorted_state_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
