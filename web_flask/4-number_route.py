#!/usr/bin/python3
"""Flask instance"""
from flask import Flask


app = Flask(__name__)
"""The Flask instance"""

@app.route("/", strict_slashes=False)
def hello():
    """returns a simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """returns HBNB string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    """Function that returns a C string"""
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text="is cool"):
    """Function that returns a Python string"""
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """returns a string only if n is a number"""
    if type(n) == int:
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)