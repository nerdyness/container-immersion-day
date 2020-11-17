from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def greeting():
    return os.environ['GREETING']
