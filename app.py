from flask import Flask, make_response
from random import randint

from flask.scaffold import F
app = Flask(__name__)


@app.route('/error/')
def server_error():
    response = make_response("error", 500)
    response.headers['edge-control'] = "max-age = 300"
    response.headers['cache-control'] = "max-age = 600"
    response.headers['x-flask'] = "true"
    return response


@app.route('/good/')
def hello_world():
    return 'flask hello world!', 200


@app.route('/random/')
def random():
    if randint(0, 1):
        return "random ok flask", 200
    else:
        return 'random error flask', 500
