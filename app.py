from flask import Flask
app = Flask(__name__)

@app.route('/')
def server_error():
   return 'server error', 500
    
