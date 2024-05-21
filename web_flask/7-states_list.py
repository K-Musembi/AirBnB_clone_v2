#!/usr/bin/python3
"""A Flask Web App"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

unsorted_data = storage.all(State)


@app.teardown_appcontext
def remove_session(exception=None):
    """Remove current sqlalchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Render html with list of states"""

    dct = {}
    for key, obj in unsorted_data.items():
        s_id = key.split(".")[1]
        name = obj.name
        dct.update({s_id: name})

    data = {
        k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
    return render_template("7-states_list.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
