#!/usr/bin/python3
""" start web app """

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a list of state """
    state_objects = storage.all(State).values()
    data = sorted(state_objects, key=lambda state: state.name)
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def teardown(exception):
    """ remove sql session """
    storage.close()


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
