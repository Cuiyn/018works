from flask import Flask
#from app import app

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"

app.run()
