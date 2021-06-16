from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/error/')
def server_error():
   return 'flask server error', 500

@app.route('/good/')
def hello_world():
   return 'flask hello world!', 200

@app.route('/random/')
def hello_world():
   if randint(0,1):
      return "random ok flask", 200
   else:
      return 'random error flask', 500