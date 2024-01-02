#!/usr/bin/python3
""" start a flask app """

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ displays cities by state """
    state_objects = storage.all('State').values()
    states = sorted(state_objects, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ remove sql session """
    storage.close()


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
