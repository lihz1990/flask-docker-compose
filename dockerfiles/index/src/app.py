from flask import Flask, jsonify, request
import requests
from time import time
import os

app = Flask(__name__)


time_service_endpoint = os.environ.get("TIME_SERVICE")
fib_service_endpoint = os.environ.get("FIB_SERVICE")


@app.route("/")
def index():
    return "<h1>This is Index Page</h1>"


@app.route("/time")
def time_view():
    r = requests.get("http://{}/time".format(time_service_endpoint))
    return r.json()


@app.route("/fib")
def fib():
    n = request.args.get("n")
    r = requests.get("http://{}/fib?n={}".format(fib_service_endpoint, n))
    return r.json()



