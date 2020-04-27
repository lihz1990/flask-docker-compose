from flask import Flask, jsonify, request
from time import time

app = Flask(__name__)


def fib(n=10):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


@app.route("/fib")
def fib_view():

    n = request.args.get("n")
    if not n:
        return jsonify(data="not found <n>")
    return jsonify(data=fib(int(n)))
