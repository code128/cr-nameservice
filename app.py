"""
Adapted from the Hello World server. 
"""
import os
import requests
import random

from flask import Flask, render_template, jsonify

# pylint: disable=C0103
app = Flask(__name__)

groupNamesFile = "data/groupnames.txt"
nickNamesFile = "data/nicknames.txt"


def get_metadata(item_name):
    metadata_url = "http://metadata.google.internal/computeMetadata/v1/"
    headers = {"Metadata-Flavor": "Google"}

    try:
        r = requests.get(metadata_url + item_name, headers=headers)
        return r.text
    except:
        return "Unavailable"


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""

    return render_template("index.html")


@app.route("/groupname")
def groupname():
    """Return a random groupname."""
    return jsonify(name=getRandomLine(groupNamesFile))


@app.route("/nickname")
def nickname():
    """Return a random nickname."""
    return jsonify(name=getRandomLine(nickNamesFile))


def getRandomLine(filename):
    """Return a random line from a file."""
    lines = open(filename).read().splitlines()
    return random.choice(lines)


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=False, port=server_port, host="0.0.0.0")
