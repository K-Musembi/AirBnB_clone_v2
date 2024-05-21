#!/usr/bin/python3
"""A Flask Web App"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.engine.db_storage import DBStorage

app = Flask(__name__)

unsorted_data = storage.all(State)


@app.teardown_appcontext
def remove_session(exception=None):
    """Remove current sqlalchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """Render html with list of states"""

    lst = []
    dct = {}
    for key, obj in unsorted_data.items():
        s_id = key.split(".")[1]
        lst.append(s_id)
        name = obj.name

        if isinstance(storage, DBStorage):
            new_lst = obj.cities
        else:
            new_lst = obj.cities()

        new_lst.sort()
        for city in new_lst:
            lst.append(city)

        dct.update({lst: name})

    data = {
        k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
    return render_template("7-states_list.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
