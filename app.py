from flask import Flask
app = Flask(__name__)

@app.route('/error')
def server_error():
   return 'server error', 500

@app.route('/good')
def hello_world():
   return 'hello world!', 200
