#!/usr/bin/python3
"""Flask instance"""
from flask import Flask, render_template


app = Flask(__name__)
"""Flask instance"""

@app.route("/", strict_slashes=False)
def hello_route():
    """returns a simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_route_v1():
    """returns HBNB string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_route_v2(text):
    """Function that returns a C string"""
    return 'C ' + text.replace('_', ' ')



@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_route_v3(text='is cool'):
    """Function that returns a Python string"""
    return 'Python ' + text.replace('_', ' ')



@app.route("/number/<int:n>", strict_slashes=False)
def hello_route_v4(n):
    """returns a string only if n is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_route_v5(n):
    """Returns a template with the given number."""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')