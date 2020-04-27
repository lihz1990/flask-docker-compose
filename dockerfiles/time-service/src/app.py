from flask import Flask, jsonify
from time import time

app = Flask(__name__)


@app.route("/time")
def time_view():
    return jsonify(data=time())
