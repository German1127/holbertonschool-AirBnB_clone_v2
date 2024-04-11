#!/usr/bin/python3
"""flask"""
from flask import Flask


app = Flask(__name__)
"""The Flask instance"""
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
